import whois
import re


def clean_value(value):

    if isinstance(value, list):
        return value[0]

    return value


def format_date(value):

    if isinstance(value, list):
        value = value[0]

    if value:
        return value.strftime("%d-%m-%Y")

    return "N/A"


def whois_lookup(domain):

    try:
        if not re.match(r"^(?!-)(?:[A-Za-z0-9-]{1,63}\.)+[A-Za-z]{2,}$", domain):

         raise Exception(
        "Please enter a valid domain name (example: google.com)."
    )

        data = whois.whois(domain)

        if not data:
            raise Exception("Unable to retrieve WHOIS information.")

        # -------------------------------
        # Validate WHOIS response
        # -------------------------------

        valid = any([

            getattr(data, "registrar", None),

            getattr(data, "creation_date", None),

            getattr(data, "expiration_date", None),

            getattr(data, "name_servers", None),

            getattr(data, "domain_name", None)

        ])

        if not valid:

            raise Exception(
                "No WHOIS record exists for the supplied domain."
            )

        report = {

            "domain": clean_value(getattr(data, "domain_name", None)) or domain,

            "registrar": clean_value(getattr(data, "registrar", None)) or "N/A",

            "creation_date": format_date(getattr(data, "creation_date", None)),

            "expiration_date": format_date(getattr(data, "expiration_date", None)),

            "updated_date": format_date(getattr(data, "updated_date", None)),

            "registrant": clean_value(getattr(data, "name", None)) or "N/A",

            "organization": clean_value(getattr(data, "org", None)) or "N/A",

            "email": clean_value(getattr(data, "emails", None)) or "N/A",

            "phone": clean_value(getattr(data, "phone", None)) or "N/A",

            "address": clean_value(getattr(data, "address", None)) or "N/A",

            "city": clean_value(getattr(data, "city", None)) or "N/A",

            "state": clean_value(getattr(data, "state", None)) or "N/A",

            "country": clean_value(getattr(data, "country", None)) or "N/A",

            "zipcode": clean_value(getattr(data, "zipcode", None)) or "N/A",

            "dnssec": clean_value(getattr(data, "dnssec", None)) or "N/A",

            "status": clean_value(getattr(data, "status", None)) or "N/A",

            "name_servers": sorted(
                list(data.name_servers)
            ) if getattr(data, "name_servers", None) else []

        }

        return report

    except whois.parser.PywhoisError:

        raise Exception(
            "The supplied domain does not exist or WHOIS information is unavailable."
        )

    except Exception as e:

        raise Exception(
            f"WHOIS lookup failed: {e}"
        )