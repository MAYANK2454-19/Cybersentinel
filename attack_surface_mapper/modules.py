from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from ping_tool.ping import ping_host
from scanner.scanner import run_scan
from dns_tool.dns_lookup import dns_lookup
from whois_tool.whois_lookup import whois_lookup
from ssl_analyzer.ssl_lookup import analyze_ssl
from security_headers.headers import analyze_headers
from geolocation.geolocation import ip_lookup
from subdomain_finder.subfinder import find_subdomains
from technology_detector.tech_detect import detect_technology
import socket


def execute_modules(domain, selected):

    results = {}

    jobs = {}

    with ThreadPoolExecutor(max_workers=8) as executor:

        if "ping" in selected:
            jobs[
                executor.submit(
                    ping_host,
                    domain
                )
            ] = "ping"

        if "ports" in selected:
            jobs[
                executor.submit(
                    run_scan,
                    domain,
                    1,
                    1000
                )
            ] = "ports"

        if "dns" in selected:
            jobs[
                executor.submit(
                    dns_lookup,
                    domain
                )
            ] = "dns"

        if "whois" in selected:
            jobs[
                executor.submit(
                    whois_lookup,
                    domain
                )
            ] = "whois"

        if "ssl" in selected:
            jobs[
                executor.submit(
                    analyze_ssl,
                    domain
                )
            ] = "ssl"

        if "headers" in selected:
            jobs[
                executor.submit(
                    analyze_headers,
                    domain
                )
            ] = "headers"

        if "subdomains" in selected:
            jobs[
                executor.submit(
                    find_subdomains,
                    domain
                )
            ] = "subdomains"

        if "geo" in selected:

            ip = socket.gethostbyname(domain)

            jobs[
                executor.submit(
                    ip_lookup,
                    ip
                )
            ] = "geo"
        if "technology" in selected:

            jobs[
                executor.submit(
                    detect_technology,
                    domain
                )
            ]="technology"
            
        for future in as_completed(jobs):

            module = jobs[future]

            try:

                results[module] = future.result()

            except Exception as e:

                results[module] = {

                    "error": str(e)

                }

    return results