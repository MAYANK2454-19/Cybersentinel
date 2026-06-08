import socket
from cyber_app.cyber_scanner.scanner.dns_lookup import get_ip
def port_scan(ip :str ,hostname : str ,start_port : int , end_port : int, all_ports : list) -> list[int]:
    try :
        open_ports = []
        for port in range(start_port, end_port + 1):
            sock = socket.socket()
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        all_ports.extend(open_ports)
        return open_ports
    except socket.gaierror :
        print(f"{hostname} is not a valid hostname.")
        return []