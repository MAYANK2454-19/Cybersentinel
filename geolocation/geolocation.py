import re
import requests


def ip_lookup(ip: str) -> dict:

    ip = ip.strip()

    # Basic IPv4 validation
    pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"

    if not re.match(pattern, ip):
        raise Exception(
            "Please enter a valid IPv4 address."
        )

    # Check each octet
    octets = ip.split(".")

    for octet in octets:

        if int(octet) > 255:

            raise Exception(
                "Please enter a valid IPv4 address."
            )

    try:

        url = f"http://ip-api.com/json/{ip}"

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if data.get("status") != "success":

            raise Exception(
                data.get("message", "Unable to locate the supplied IP address.")
            )

        return {

            "ip": data.get("query", "N/A"),

            "country": data.get("country", "N/A"),

            "region": data.get("regionName", "N/A"),

            "city": data.get("city", "N/A"),

            "zip": data.get("zip", "N/A"),

            "isp": data.get("isp", "N/A"),

            "org": data.get("org", "N/A"),

            "timezone": data.get("timezone", "N/A"),

            "latitude": data.get("lat", "N/A"),

            "longitude": data.get("lon", "N/A")

        }

    except requests.exceptions.Timeout:

        raise Exception(
            "The geolocation service timed out."
        )

    except requests.exceptions.ConnectionError:

        raise Exception(
            "Unable to connect to the geolocation service."
        )

    except requests.exceptions.HTTPError:

        raise Exception(
            "The geolocation service returned an unexpected response."
        )

    except Exception as e:

        raise Exception(
            f"Geolocation lookup failed: {e}"
        )