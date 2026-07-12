import ssl
import socket
import re

from datetime import datetime, UTC


def validate_domain(domain):

    domain = domain.strip().lower()

    pattern = r"^(?!-)(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,}$"

    if not re.match(pattern, domain):

        raise Exception(
            "Please enter a valid domain name."
        )

    return domain


def analyze_ssl(domain):

    domain = validate_domain(domain)

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (domain, 443),
            timeout=5
        ) as sock:

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

                start_date = datetime.strptime(
                    cert["notBefore"],
                    "%b %d %H:%M:%S %Y %Z"
                )

                end_date = datetime.strptime(
                    cert["notAfter"],
                    "%b %d %H:%M:%S %Y %Z"
                )

                days_remaining = (
                    end_date.replace(tzinfo=UTC)
                    - datetime.now(UTC)
                ).days

                san = []

                for entry in cert.get(
                    "subjectAltName",
                    []
                ):

                    san.append(entry[1])

                return {

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

    except socket.gaierror:

        raise Exception(
            "Unable to resolve the supplied domain."
        )

    except TimeoutError:

        raise Exception(
            "Connection timed out while retrieving the SSL certificate."
        )

    except ssl.SSLError:

        raise Exception(
            "The target does not provide a valid SSL/TLS certificate."
        )

    except ConnectionRefusedError:

        raise Exception(
            "The HTTPS service is unavailable on the target."
        )

    except Exception as e:

        raise Exception(
            f"SSL inspection failed: {e}"
        )


if __name__ == "__main__":

    print(
        analyze_ssl("google.com")
    )