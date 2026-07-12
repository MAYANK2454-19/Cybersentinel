import re
import socket
import requests
from concurrent.futures import ThreadPoolExecutor


# ---------------------------------------
# Domain Validation
# ---------------------------------------

def validate_domain(domain):

    domain = domain.strip().lower()

    pattern = r"^(?!-)(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,}$"

    if not re.match(pattern, domain):

        raise Exception(
            "Please enter a valid domain name."
        )

    return domain


# ---------------------------------------
# CRT.SH
# ---------------------------------------

def get_crtsh(domain):

    subdomains = set()

    try:

        url = f"https://crt.sh/?q=%25.{domain}&output=json"

        response = requests.get(
            url,
            timeout=30,
            headers={
                "User-Agent": "CyberSentinel"
            }
        )

        response.raise_for_status()

        data = response.json()

        for item in data:

            names = item.get(
                "name_value",
                ""
            ).split("\n")

            for name in names:

                name = name.strip().lower()

                if domain in name:

                    subdomains.add(name)

    except:

        pass

    return subdomains


# ---------------------------------------
# HackerTarget
# ---------------------------------------

def get_hackertarget(domain):

    subdomains = set()

    try:

        url = (
            "https://api.hackertarget.com/"
            f"hostsearch/?q={domain}"
        )

        response = requests.get(
            url,
            timeout=20
        )

        response.raise_for_status()

        for line in response.text.splitlines():

            if "," in line:

                subdomains.add(
                    line.split(",")[0].strip()
                )

    except:

        pass

    return subdomains


# ---------------------------------------
# AlienVault
# ---------------------------------------

def get_otx(domain):

    subdomains = set()

    try:

        url = (
            "https://otx.alienvault.com/"
            "api/v1/indicators/domain/"
            f"{domain}/passive_dns"
        )

        response = requests.get(
            url,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        for item in data.get(
            "passive_dns",
            []
        ):

            hostname = item.get("hostname")

            if hostname:

                subdomains.add(hostname)

    except:

        pass

    return subdomains


# ---------------------------------------
# DNS Validation
# ---------------------------------------

def is_live(subdomain):

    try:

        socket.gethostbyname(subdomain)

        return subdomain

    except:

        return None


def validate_subdomains(subdomains):

    live = []

    with ThreadPoolExecutor(max_workers=50) as executor:

        for result in executor.map(
            is_live,
            subdomains
        ):

            if result:

                live.append(result)

    return live


# ---------------------------------------
# Main Function
# ---------------------------------------

def find_subdomains(domain):

    domain = validate_domain(domain)

    try:

        all_subdomains = set()

        all_subdomains.update(
            get_crtsh(domain)
        )

        all_subdomains.update(
            get_hackertarget(domain)
        )

        all_subdomains.update(
            get_otx(domain)
        )

        if len(all_subdomains) == 0:

            raise Exception(
                "No subdomains were discovered for this domain."
            )

        live = validate_subdomains(
            all_subdomains
        )

        return {

            "domain": domain,

            "total_found": len(all_subdomains),

            "live_count": len(live),

            "dead_count":
                len(all_subdomains) - len(live),

            "subdomains":
                sorted(all_subdomains),

            "live_subdomains":
                sorted(live)

        }

    except Exception as e:

        raise Exception(
            f"Subdomain enumeration failed: {e}"
        )