from ping_tool.ping import ping_host
from dns_tool.dns_lookup import dns_lookup
from whois_tool.whois_lookup import whois_lookup
from ssl_analyzer.ssl_lookup import analyze_ssl
from security_headers.headers import analyze_headers
from subdomain_finder.subfinder import find_subdomains
from scanner.scanner import run_scan
from geolocation.geolocation import ip_lookup


def unified_scan(
    target,
    modules,
    start_port=1,
    end_port=1000
):

    report = {

        "target": target,

        "modules": {},

        "summary": {

            "selected": len(modules),

            "successful": 0,

            "failed": 0

        }

    }

    # ---------------- PING ----------------

    if "ping" in modules:

        try:

            result = ping_host(target)

            report["modules"]["ping"] = result

            if "error" in result:

                report["summary"]["failed"] += 1

            else:

                report["summary"]["successful"] += 1

        except Exception as e:

            report["modules"]["ping"] = {

                "error": str(e)

            }

            report["summary"]["failed"] += 1

    # ---------------- DNS ----------------

    if "dns" in modules:

        try:

            result = dns_lookup(target)

            report["modules"]["dns"] = result

            if "error" in result:

                report["summary"]["failed"] += 1

            else:

                report["summary"]["successful"] += 1

        except Exception as e:

            report["modules"]["dns"] = {

                "error": str(e)

            }

            report["summary"]["failed"] += 1

    # ---------------- WHOIS ----------------

    if "whois" in modules:

        try:

            result = whois_lookup(target)

            report["modules"]["whois"] = result

            if "error" in result:

                report["summary"]["failed"] += 1

            else:

                report["summary"]["successful"] += 1

        except Exception as e:

            report["modules"]["whois"] = {

                "error": str(e)

            }

            report["summary"]["failed"] += 1

    # ---------------- SSL ----------------

    if "ssl" in modules:

        try:

            result = analyze_ssl(target)

            report["modules"]["ssl"] = result

            if "error" in result:

                report["summary"]["failed"] += 1

            else:

                report["summary"]["successful"] += 1

        except Exception as e:

            report["modules"]["ssl"] = {

                "error": str(e)

            }

            report["summary"]["failed"] += 1

    # ---------------- SECURITY HEADERS ----------------

    if "headers" in modules:

        try:

            result = analyze_headers(target)

            report["modules"]["headers"] = result

            if "error" in result:

                report["summary"]["failed"] += 1

            else:

                report["summary"]["successful"] += 1

        except Exception as e:

            report["modules"]["headers"] = {

                "error": str(e)

            }

            report["summary"]["failed"] += 1

    # ---------------- SUBDOMAINS ----------------

    if "subdomains" in modules:

        try:

            result = find_subdomains(target)

            report["modules"]["subdomains"] = result

            if "error" in result:

                report["summary"]["failed"] += 1

            else:

                report["summary"]["successful"] += 1

        except Exception as e:

            report["modules"]["subdomains"] = {

                "error": str(e)

            }

            report["summary"]["failed"] += 1

    # ---------------- PORT SCANNER ----------------

    if "ports" in modules:

        try:

            result = run_scan(

                target,

                int(start_port),

                int(end_port)

            )

            report["modules"]["ports"] = result

            if "error" in result:

                report["summary"]["failed"] += 1

            else:

                report["summary"]["successful"] += 1

        except Exception as e:

            report["modules"]["ports"] = {

                "error": str(e)

            }

            report["summary"]["failed"] += 1

    # ---------------- GEOLOCATION ----------------

    if "geo" in modules:

        try:

            if (

                "ports" in report["modules"]

                and

                "error" not in report["modules"]["ports"]

            ):

                ip = report["modules"]["ports"]["ip"]

            else:

                ip = target

            result = ip_lookup(ip)

            report["modules"]["geo"] = result

            if "error" in result:

                report["summary"]["failed"] += 1

            else:

                report["summary"]["successful"] += 1

        except Exception as e:

            report["modules"]["geo"] = {

                "error": str(e)

            }

            report["summary"]["failed"] += 1

    return report