import requests


def ip_lookup(ip: str) -> dict:

    url = f"http://ip-api.com/json/{ip}"

    response = requests.get(url, timeout=10)

    data = response.json()

    if data["status"] != "success":

        return {
            "error": "Invalid IP Address"
        }

    return {

        "ip": data["query"],
        "country": data["country"],
        "region": data["regionName"],
        "city": data["city"],
        "zip": data["zip"],
        "isp": data["isp"],
        "org": data["org"],
        "timezone": data["timezone"],
        "latitude": data["lat"],
        "longitude": data["lon"]

    }