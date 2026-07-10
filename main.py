from flask import Flask, render_template, request
from scanner.scanner import run_scan 
from ping_tool.ping import ping_host
from whois_tool.whois_lookup import whois_lookup as whois_service
from dns_tool.dns_lookup import dns_lookup as dns_service
from ssl_analyzer.ssl_lookup import analyze_ssl as ssl_service
from security_headers.headers import analyze_headers as headers_service
from geolocation.geolocation import ip_lookup as geo_service
from subdomain_finder.subfinder import find_subdomains as subdomain_service

import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/portscan", methods=["GET", "POST"])
def portscan():

    if request.method == "POST":

        try:

            hostname = request.form["hostname"].strip()
            start_port = int(request.form["start_port"])
            end_port = int(request.form["end_port"])

            if not hostname:
                raise ValueError("Please enter a valid hostname.")

            report = run_scan(
                hostname,
                start_port,
                end_port
            )

            return render_template(
                "result.html",
                report=report
            )

        except Exception as e:

            return render_template(
                "error.html",
                message=str(e)
            )

    return render_template("portscan.html")


@app.route("/ping", methods=["GET", "POST"])
def ping():

    if request.method == "POST":

        try:

            hostname = request.form["hostname"].strip()

            if not hostname:
                raise ValueError("Please enter a valid hostname or IP address.")

            report = ping_host(hostname)

            return render_template(
                "ping_result.html",
                report=report
            )

        except ValueError as e:

            return render_template(
                "error.html",
                message=str(e)
            )

        except Exception:

            return render_template(
                "error.html",
                message="Unable to ping the target. Please verify the hostname and try again."
            )

    return render_template("ping.html")

@app.route("/geo", methods=["GET", "POST"])
def geolocation():

    if request.method == "POST":

        try:

            ip = request.form["ip"].strip()

            if not ip:
                raise ValueError("Please enter a valid IP address.")

            report = geo_service(ip)

            return render_template(
                "geolocation_result.html",
                report=report
            )

        except ValueError as e:

            return render_template(
                "error.html",
                message=str(e)
            )

        except Exception:

            return render_template(
                "error.html",
                message="Unable to retrieve geolocation information."
            )

    return render_template("geolocation.html")
@app.route("/subdomain", methods=["GET", "POST"])
def subdomain():

    if request.method == "POST":

        try:

            domain = request.form["domain"].strip()

            if not domain:
                raise ValueError("Please enter a valid domain.")

            report = subdomain_service(domain)

            return render_template(
                "subdomain_result.html",
                report=report
            )

        except ValueError as e:

            return render_template(
                "error.html",
                message=str(e)
            )

        except Exception:

            return render_template(
                "error.html",
                message="Unable to enumerate subdomains for the specified domain."
            )

    return render_template("subdomain.html")

@app.route("/whois", methods=["GET", "POST"])
def whois_look():

    if request.method == "POST":

        try:

            domain = request.form["domain"].strip()

            if not domain:
                raise ValueError("Please enter a valid domain.")

            report = whois_service(domain)

            return render_template(
                "whois_result.html",
                report=report
            )

        except ValueError as e:

            return render_template(
                "error.html",
                message=str(e)
            )

        except Exception:

            return render_template(
                "error.html",
                message="WHOIS lookup failed. Registrar information could not be retrieved."
            )

    return render_template("whois_index.html")

@app.route("/dns", methods=["GET", "POST"])
def dns_look():

    if request.method == "POST":

        try:

            domain = request.form["domain"].strip()

            if not domain:
                raise ValueError("Please enter a valid domain.")

            report = dns_service(domain)

            return render_template(
                "dns_result.html",
                report=report
            )

        except ValueError as e:

            return render_template(
                "error.html",
                message=str(e)
            )

        except Exception:

            return render_template(
                "error.html",
                message="DNS lookup failed. The domain may not exist or DNS servers are unreachable."
            )

    return render_template("dns_index.html")
@app.route("/ssl", methods=["GET", "POST"])
def ssl_look():

    if request.method == "POST":

        try:

            domain = request.form["domain"].strip()

            if not domain:
                raise ValueError("Please enter a valid domain.")

            report = ssl_service(domain)

            if isinstance(report, dict) and "error" in report:
                return render_template(
                    "error.html",
                    message=report["error"]
                )

            return render_template(
                "ssl_result.html",
                report=report
            )

        except ValueError as e:

            return render_template(
                "error.html",
                message=str(e)
            )

        except Exception as e:

            print(f"[SSL ERROR] {e}")

            return render_template(
                "error.html",
                message=f"SSL inspection failed: {e}"
            )

    return render_template("ssl_index.html")
@app.route("/headers", methods=["GET", "POST"])
def security_headers():

    if request.method == "POST":

        try:

            domain = request.form["domain"].strip()

            if not domain:
                raise ValueError("Please enter a valid domain.")

            report = headers_service(domain)

            if isinstance(report, dict) and "error" in report:
                return render_template(
                    "error.html",
                    message=report["error"]
                )

            return render_template(
                "headers_result.html",
                report=report
            )

        except ValueError as e:

            return render_template(
                "error.html",
                message=str(e)
            )

        except Exception as e:

            print(f"[HEADERS ERROR] {e}")

            return render_template(
                "error.html",
                message=f"Security Header Analysis failed: {e}"
            )

    return render_template("headers_index.html")
@app.route("/test-error")
def test_error():

    return render_template(
        "error.html",
        message="Unable to resolve the target host."
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 4000)),
        debug=True
    )