import socket
import time


def ping_host(hostname: str) -> dict:

    try:
        ip = socket.gethostbyname(hostname)

        latencies = []

        packets_sent = 4
        packets_received = 0

        for _ in range(4):

            start = time.time()

            sock = socket.create_connection(
                (hostname, 80),
                timeout=5
            )

            end = time.time()

            sock.close()

            latency = round((end - start) * 1000, 3)

            latencies.append(latency)

            packets_received += 1

        packet_loss = (
            (packets_sent - packets_received)
            / packets_sent
        ) * 100

        rtt_min = min(latencies)
        rtt_avg = round(sum(latencies) / len(latencies), 3)
        rtt_max = max(latencies)

        jitter = round(
            max(latencies) - min(latencies),
            3
        )

        total_time = round(sum(latencies), 3)

        return {
            "host": hostname,
            "ip": ip,
            "status": "Reachable",
            "packets_transmitted": str(packets_sent),
            "packets_received": str(packets_received),
            "packet_loss": f"{packet_loss:.0f}%",
            "total_time": f"{total_time} ms",
            "rtt_min": f"{rtt_min} ms",
            "rtt_avg": f"{rtt_avg} ms",
            "rtt_max": f"{rtt_max} ms",
            "jitter": f"{jitter} ms"
        }

    except Exception:

        return {
            "host": hostname,
            "ip": "N/A",
            "status": "Unreachable",
            "packets_transmitted": "4",
            "packets_received": "0",
            "packet_loss": "100%",
            "total_time": "0 ms",
            "rtt_min": "0 ms",
            "rtt_avg": "0 ms",
            "rtt_max": "0 ms",
            "jitter": "0 ms"
        }