import subprocess

def ping_host(hostname: str) -> dict:
    ip = None
    stats = []
    rtt_stats = []

    try:
        output = subprocess.run(
            ["ping", "-c", "4", hostname],
            capture_output=True,
            text=True,
            timeout=10
    )
    except Exception as e:
        return {
            "error": str(e)
    }
    if output.returncode != 0:
        return {
        "error": f"Unable to reach {hostname}"
    }

    lines = output.stdout.split("\n")

    for line in lines :
        if line.startswith("PING"):
            ip = line.split("(")[1].split(")")[0]
        if "packets transmitted" in line:
            stats = line.split(",")
            
        if "rtt" in line:
            rtt_values = line.split("=")[1].strip().replace("ms", "")
            rtt_stats = rtt_values.split("/")
            



    stats_output = {
    "host": hostname,
    "ip": ip,
    "status": "Reachable",
    "packets_transmitted": stats[0].split()[0],
    "packets_received": stats[1].split()[0],
    "packet_loss": stats[2].split()[0],
    "total_time": stats[3].split()[1].replace("ms", "") + " ms" ,
    "rtt_min": rtt_stats[0] + " ms",
    "rtt_avg": rtt_stats[1] + " ms",
    "rtt_max": rtt_stats[2] + " ms",
    "jitter": rtt_stats[3].strip() + " ms"
}

    return stats_output