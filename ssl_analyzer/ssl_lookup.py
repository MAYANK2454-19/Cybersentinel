import ssl
import socket
from datetime import datetime


def analyze_ssl(domain):

    try:

        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=5) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as ssock:

                cert = ssock.getpeercert()

                issuer = dict(
                    x[0] for x in cert["issuer"]
                )

                subject = dict(
                    x[0] for x in cert["subject"]
                )

                valid_from = cert["notBefore"]
                valid_until = cert["notAfter"]

                start_date = datetime.strptime(
                    valid_from,
                    "%b %d %H:%M:%S %Y %Z"
                )

                end_date = datetime.strptime(
                    valid_until,
                    "%b %d %H:%M:%S %Y %Z"
                )

                days_remaining = (
                    end_date - datetime.utcnow()
                ).days

                san = []

                if "subjectAltName" in cert:

                    for entry in cert["subjectAltName"]:

                        san.append(entry[1])

                report = {

                    "domain": domain,

                    "subject": subject.get(
                        "commonName",
                        "N/A"
                    ),

                    "issuer": issuer.get(
                        "commonName",
                        "N/A"
                    ),

                    "valid_from": start_date.strftime(
                        "%d-%m-%Y"
                    ),

                    "valid_until": end_date.strftime(
                        "%d-%m-%Y"
                    ),

                    "days_remaining": days_remaining,

                    "tls_version": ssock.version(),

                    "san": san

                }

                return report

    except Exception as e:

        return {
            "error": str(e)
        }