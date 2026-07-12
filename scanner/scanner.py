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

    hostname = hostname.strip()

    if not hostname:

        raise Exception(
            "Please enter a valid hostname."
        )

    if start_port < 1 or end_port > 65535:

        raise Exception(
            "Ports must be between 1 and 65535."
        )

    if start_port > end_port:

        raise Exception(
            "Start port cannot be greater than end port."
        )

    start_time = time.time()

    ip = get_ip(hostname)

    if ip is None:

        raise Exception(
            "Unable to resolve the supplied hostname."
        )

    try:

        socket.gethostbyname(hostname)

        host_status = "Online"

    except socket.gaierror:

        raise Exception(
            "Unable to resolve the supplied hostname."
        )

    except Exception as e:

        raise Exception(
            f"DNS resolution failed: {e}"
        )

    dns_reverse = reverse_lookup(ip)

    all_ports = []

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

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    all_ports.sort()

    if len(all_ports) == 0:

        raise Exception(
            "No open ports were discovered in the specified range."
        )

    results = {}

    for port in all_ports:

        try:

            if port == 443:

                raw = get_https_banner(
                    ip,
                    hostname,
                    port
                )

            else:

                raw = get_banner(
                    ip,
                    hostname,
                    port
                )

            headers = head_parser(raw) if raw else {}

            server = headers.get(
                "server",
                ""
            ).lower()

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

    scan_time = round(
        time.time() - start_time,
        2
    )

    return {

        "hostname": hostname,

        "ip": ip,

        "reverse_dns": dns_reverse,

        "host_status": host_status,

        "scan_time": scan_time,

        "open_ports": results

    }