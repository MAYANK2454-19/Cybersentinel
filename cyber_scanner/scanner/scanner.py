import threading
from cyber_app.cyber_scanner.scanner.functions import get_banner, get_ip
from cyber_app.cyber_scanner.scanner.open_ports import port_scan
from cyber_app.cyber_scanner.scanner.detect_service import detect_service
from cyber_app.cyber_scanner.scanner.header_parser import head_parser
from cyber_app.cyber_scanner.scanner.https_banner import get_https_banner
from cyber_app.cyber_scanner.scanner.reverse_lookup import reverse_lookup

def run_scan(hostname: str) -> dict:
    ip = get_ip(hostname)
    if ip is None:
        return {"error": "Unable to resolve hostname"}
    all_ports: list[int] = []
    CHUNK_SIZE = 50
    dns_reverse = reverse_lookup(ip)
    #threads

    threads = []

    for start in range(1, 501, CHUNK_SIZE):
        t = threading.Thread(
            target=port_scan,
            args=(ip, hostname, start, start + CHUNK_SIZE - 1, all_ports)
        )

        threads.append(t)

    #threaing start 
    for t in threads:
        t.start()

    #threads waiting
    for t in threads:
        t.join()

    all_ports.sort()
    

    results = {}

    for port in all_ports:
        results[port] = {
            "service": detect_service(port),
            "headers": head_parser(get_banner(ip, hostname, port)) if port != 443 else head_parser(get_https_banner(ip, hostname, port))
            
        }
    report = {"hostname": hostname, 
            "ip": ip, 
            "reverse_dns" : dns_reverse,
            "open_ports": results}
    
    return report