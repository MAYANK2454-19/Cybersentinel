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
        "modules": {}
    }

    if "ping" in modules:
        report["modules"]["ping"] = ping_host(target)

    if "dns" in modules:
        report["modules"]["dns"] = dns_lookup(target)

    if "whois" in modules:
        report["modules"]["whois"] = whois_lookup(target)

    if "ssl" in modules:
        report["modules"]["ssl"] = analyze_ssl(target)

    if "headers" in modules:
        report["modules"]["headers"] = analyze_headers(target)

    if "subdomains" in modules:
        report["modules"]["subdomains"] = find_subdomains(target)

    if "ports" in modules:
        report["modules"]["ports"] = run_scan(
            target,
            int(start_port),
            int(end_port)
        )

    if "geo" in modules:

        try:

            ip = report["modules"]["ports"]["ip"]

        except:

            ip = target

        report["modules"]["geo"] = ip_lookup(ip)

    return report