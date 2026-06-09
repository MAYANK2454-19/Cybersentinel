import threading
import socket
import time

from .network_utils import get_banner, get_ip
from .port_scan import port_scan
from .detect_service import detect_service
from .header_parser import head_parser
from .https_banner import get_https_banner
from .reverse_lookup import reverse_lookup


def run_scan(
    hostname: str,
    start_port: int,
    end_port: int
) -> dict:

    start_time = time.time()

    ip = get_ip(hostname)

    if ip is None:
        return {"error": "Unable to resolve hostname"}

    try:
        socket.gethostbyname(hostname)
        host_status = "Online"
    except Exception:
        host_status = "Offline"

    dns_reverse = reverse_lookup(ip)

    all_ports: list[int] = []

    CHUNK_SIZE = 25

    threads = []

    for start in range(start_port, end_port + 1, CHUNK_SIZE):

        t = threading.Thread(
            target=port_scan,
            args=(
                ip,
                hostname,
                start,
                min(start + CHUNK_SIZE - 1, end_port),
                all_ports
            )
        )

        threads.append(t)

    # Start threads
    for t in threads:
        t.start()

    # Wait for completion
    for t in threads:
        t.join()

    all_ports.sort()

    results = {}

    for port in all_ports:

        try:

            if port == 443:
                raw = get_https_banner(ip, hostname, port)
            else:
                raw = get_banner(ip, hostname, port)

            headers = head_parser(raw) if raw else {}

            server = headers.get("server", "").lower()

            if "apache" in server:
                tech = "Apache"

            elif "nginx" in server:
                tech = "Nginx"

            elif "gws" in server:
                tech = "Google Web Server"

            elif "iis" in server:
                tech = "Microsoft IIS"

            elif server == "":
                tech = "Unknown"

            else:
                tech = server

            results[port] = {
                "service": detect_service(port),
                "technology": tech,
                "headers": headers
            }

        except Exception as e:

            results[port] = {
                "service": detect_service(port),
                "technology": "Unknown",
                "headers": {
                    "error": str(e)
                }
            }

    scan_time = round(time.time() - start_time, 2)

    report = {
        "hostname": hostname,
        "ip": ip,
        "reverse_dns": dns_reverse,
        "host_status": host_status,
        "scan_time": scan_time,
        "open_ports": results
    }

    return report