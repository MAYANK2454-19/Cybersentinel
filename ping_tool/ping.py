import socket
import time
import re


def validate_target(target):

    target = target.strip()

    if not target:
        raise Exception(
            "Please enter a hostname or IP address."
        )

    ipv4 = r"^(?:\d{1,3}\.){3}\d{1,3}$"

    if re.match(ipv4, target):

        for part in target.split("."):

            if int(part) > 255:

                raise Exception(
                    "Please enter a valid IPv4 address."
                )

    return target


def ping_host(hostname):

    hostname = validate_target(hostname)

    try:

        ip = socket.gethostbyname(hostname)

    except socket.gaierror:

        raise Exception(
            "Unable to resolve the supplied hostname."
        )

    except Exception as e:

        raise Exception(
            f"DNS resolution failed: {e}"
        )

    ports = [80, 443, 22]

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

        except OSError:

            continue

    if connected_port is None:

        raise Exception(
            "Host is unreachable or no common TCP service is responding."
        )

    rtts = []

    packets_sent = 4

    packets_received = 0

    for _ in range(packets_sent):

        try:

            start = time.perf_counter()

            sock = socket.create_connection(
                (hostname, connected_port),
                timeout=3
            )

            end = time.perf_counter()

            sock.close()

            rtt = (end - start) * 1000

            rtts.append(rtt)

            packets_received += 1

        except OSError:

            continue

    if packets_received == 0:

        raise Exception(
            "No responses were received from the target."
        )

    packet_loss = (
        (packets_sent - packets_received)
        / packets_sent
    ) * 100

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