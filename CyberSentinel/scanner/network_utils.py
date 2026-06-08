import socket

def get_ip(target):
    try :
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror :
        print(f"{target} is not a valid hostname.")
        return None
def scan_port(target, port):
    try :
        ip = get_ip(target)
        if ip is None:
            return None
        sock=socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip,port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except socket.gaierror :
        print(f"{target} is not a valid hostname.")
        return None
def get_banner(ip,hostname, port):
    try :
        
        if ip is None:
            return None 
        msg = f"HEAD / HTTP/1.1\r\nHost: {hostname}\r\n\r\n"
        sock=socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip,port))
        if result == 0 :
            sock.send(msg.encode())
            banner = sock.recv(1024)
            sock.close()
            return banner.decode(errors='ignore')
        else:
            sock.close()
            return None
    except socket.gaierror :
        print(f"{hostname} is not a valid hostname.")
        return None