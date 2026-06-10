import requests
import socket
from concurrent.futures import ThreadPoolExecutor


# -----------------------------
# CRT.SH
# -----------------------------

def get_crtsh(domain):

    subdomains = set()

    try:

        url = f"https://crt.sh/?q=%25.{domain}&output=json"

        response = requests.get(
            url,
            timeout=30,
            headers={"User-Agent": "CyberSentinel"}
        )

        if response.status_code == 200:

            data = response.json()

            for item in data:

                names = item.get("name_value", "").split("\n")

                for name in names:

                    name = name.strip().lower()

                    if domain in name:
                        subdomains.add(name)

    except Exception:
        pass

    return subdomains


# -----------------------------
# HACKERTARGET
# -----------------------------

def get_hackertarget(domain):

    subdomains = set()

    try:

        url = (
            f"https://api.hackertarget.com/"
            f"hostsearch/?q={domain}"
        )

        response = requests.get(url, timeout=20)

        if response.status_code == 200:

            lines = response.text.splitlines()

            for line in lines:

                if "," in line:

                    subdomain = line.split(",")[0].strip()

                    subdomains.add(subdomain)

    except Exception:
        pass

    return subdomains


# -----------------------------
# ALIENVAULT OTX
# -----------------------------

def get_otx(domain):

    subdomains = set()

    try:

        url = (
            f"https://otx.alienvault.com/"
            f"api/v1/indicators/domain/"
            f"{domain}/passive_dns"
        )

        response = requests.get(url, timeout=30)

        if response.status_code == 200:

            data = response.json()

            for item in data.get("passive_dns", []):

                hostname = item.get("hostname")

                if hostname:
                    subdomains.add(hostname)

    except Exception:
        pass

    return subdomains


# -----------------------------
# DNS VALIDATION
# -----------------------------

def is_live(subdomain):

    try:

        socket.gethostbyname(subdomain)

        return subdomain

    except:

        return None


def validate_subdomains(subdomains):

    live_subdomains = []

    with ThreadPoolExecutor(max_workers=50) as executor:

        results = executor.map(
            is_live,
            subdomains
        )

        for result in results:

            if result:
                live_subdomains.append(result)

    return live_subdomains


# -----------------------------
# MAIN FUNCTION
# -----------------------------

def find_subdomains(domain):

    all_subdomains = set()

    
    all_subdomains.update(get_crtsh(domain))

    
    all_subdomains.update(get_hackertarget(domain))

    
    all_subdomains.update(get_otx(domain))

   
    live_subdomains = validate_subdomains(
        all_subdomains
    )

    return {

        "domain": domain,

        "total_found":
        len(all_subdomains),

        "live_count":
        len(live_subdomains),

        "dead_count":
        len(all_subdomains)
        - len(live_subdomains),

        "subdomains":
        sorted(all_subdomains),

        "live_subdomains":
        sorted(live_subdomains)
    }