import whois

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

        data = whois.whois(domain)

        report = {

    "domain": clean_value(data.domain_name),

    "registrar": clean_value(data.registrar),

    "creation_date": format_date(data.creation_date),

    "expiration_date": format_date(data.expiration_date),

    "updated_date": format_date(data.updated_date),

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

    "name_servers": sorted(list(data.name_servers))
    if data.name_servers
    else []

}

        return report

    except Exception as e:

        return {
            "error": str(e)
        }