from flask import Flask, render_template, request
from geolocation.geolocation import ip_lookup
from scanner.scanner import run_scan
from ping_tool.ping import ping_host
from subdomain_finder.subfinder import find_subdomains

import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/portscan", methods=["GET", "POST"])
def portscan():

    if request.method == "POST":

        hostname = request.form["hostname"]
        start_port = int(request.form["start_port"])
        end_port = int(request.form["end_port"])

        report = run_scan(
            hostname,
            start_port,
            end_port
        )

        return render_template(
            "result.html",
            report=report
        )

    return render_template("portscan.html")


@app.route("/ping", methods=["GET", "POST"])
def ping():

    if request.method == "POST":

        hostname = request.form["hostname"]

        report = ping_host(hostname)

        return render_template(
            "ping_result.html",
            report=report
        )

    return render_template("ping.html")
@app.route("/geolocation", methods=["GET", "POST"])
def geolocation():

    if request.method == "POST":

        ip = request.form["ip"]

        report = ip_lookup(ip)

        return render_template(
            "geolocation_result.html",
            report=report
        )

    return render_template(
        "geolocation.html"
    )
@app.route("/subdomain", methods=["GET", "POST"])
def subdomain():

    if request.method == "POST":

        domain = request.form["domain"]

        report = find_subdomains(domain)

        return render_template(
            "subdomain_result.html",
            report=report
        )

    return render_template("subdomain.html")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 4000)),
        debug=True
    )