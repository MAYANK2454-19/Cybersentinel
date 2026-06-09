import socket
import ssl


def get_https_banner(ip: str, hostname: str, port: int) -> str:
    msg = f"HEAD / HTTP/1.1\r\nHost: {hostname}\r\n\r\n"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        context = ssl.create_default_context()
        ssl_sock = context.wrap_socket(
            sock,
            server_hostname=hostname
        )

        ssl_sock.settimeout(3)

        ssl_sock.connect((ip, port))

        ssl_sock.send(msg.encode())

        banner = ssl_sock.recv(1024)

        return banner.decode(errors="ignore")

    except Exception:
        return ""

    finally:
        try:
            ssl_sock.close()
        except:
            pass