import dns.resolver


def get_records(domain, record_type):

    answers = dns.resolver.resolve(
        domain,
        record_type
    )

    return [str(answer) for answer in answers]


def dns_lookup(domain):

    try:

        report = {

            "domain": domain,

            "A": get_records(domain, "A"),

            "AAAA": get_records(domain, "AAAA"),

            "MX": get_records(domain, "MX"),

            "NS": get_records(domain, "NS"),

            "TXT": get_records(domain, "TXT")

        }

        return report

    except dns.resolver.NXDOMAIN:

        raise Exception(
            "The domain does not exist."
        )

    except dns.resolver.NoAnswer:

        raise Exception(
            "DNS server returned no records."
        )

    except dns.resolver.NoNameservers:

        raise Exception(
            "No DNS nameservers are available."
        )

    except Exception as e:

        raise Exception(
            f"DNS lookup failed : {e}"
        )