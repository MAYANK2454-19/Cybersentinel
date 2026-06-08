import socket

def get_ip(target: str) -> str | None:
    try :
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror :
        print(f"{target} is not a valid hostname.")
        return None
