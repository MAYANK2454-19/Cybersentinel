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
    "name_servers": sorted(list(data.name_servers))
    if data.name_servers
    else []
}

        return report

    except Exception as e:

        return {
            "error": str(e)
        }