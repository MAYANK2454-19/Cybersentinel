import dns.resolver


def get_records(domain, record_type):

    try:

        answers = dns.resolver.resolve(
            domain,
            record_type
        )

        return [str(answer) for answer in answers]

    except:

        return []


def dns_lookup(domain):

    report = {

        "domain": domain,

        "A": get_records(domain, "A"),

        "AAAA": get_records(domain, "AAAA"),

        "MX": get_records(domain, "MX"),

        "NS": get_records(domain, "NS"),

        "TXT": get_records(domain, "TXT")

    }

    return report