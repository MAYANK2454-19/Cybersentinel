import socket
import time


def ping_host(hostname: str) -> dict:

    try:
        ip = socket.gethostbyname(hostname)

    except Exception:
        return {
            "error": f"Unable to resolve {hostname}"
        }

    ports = [22,80,443]

    connected_port = None

    for port in ports:
        try:
            sock = socket.create_connection(
                (hostname, port),
                timeout=3
            )

            connected_port = port
            sock.close()
            break

        except:
            continue

    if connected_port is None:
        return {
            "error": f"Host {hostname} is unreachable"
        }

    rtts = []

    packets_sent = 4
    packets_received = 0

    for _ in range(4):

        try:
            start = time.time()

            sock = socket.create_connection(
                (hostname, connected_port),
                timeout=3
            )

            end = time.time()

            sock.close()

            rtt = (end - start) * 1000

            rtts.append(rtt)

            packets_received += 1

        except:
            pass

    packet_loss = (
        (packets_sent - packets_received)
        / packets_sent
    ) * 100

    if len(rtts) == 0:

        return {
            "error": "No responses received"
        }

    rtt_min = min(rtts)
    rtt_avg = sum(rtts) / len(rtts)
    rtt_max = max(rtts)

    jitter = rtt_max - rtt_min

    return {

        "host": hostname,
        "ip": ip,
        "status": "Reachable",

        "protocol": "TCP",
        "port_used": connected_port,

        "packets_transmitted": packets_sent,
        "packets_received": packets_received,
        "packet_loss": f"{packet_loss:.0f}%",

        "rtt_min": f"{rtt_min:.3f} ms",
        "rtt_avg": f"{rtt_avg:.3f} ms",
        "rtt_max": f"{rtt_max:.3f} ms",

        "jitter": f"{jitter:.3f} ms",

        "total_time": f"{sum(rtts):.3f} ms"
    }