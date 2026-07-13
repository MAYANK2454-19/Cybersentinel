def calculate_risk(report):

    score = 100

    findings = []

    recommendations = []

    modules = report["modules"]

    def add_finding(severity, title, description, deduction=0, recommendation=None):

        nonlocal score

        score -= deduction

        findings.append({

            "severity": severity,

            "title": title,

            "description": description

        })

        if recommendation:
            recommendations.append(recommendation)

    # ---------------- SSL ----------------

    ssl = modules.get("ssl")

    if not ssl or "error" in ssl:

        add_finding(
            "High",
            "SSL Analysis Failed",
            "Unable to inspect the SSL certificate.",
            15,
            "Verify the server's TLS configuration."
        )

    else:

        if ssl["days_remaining"] < 30:

            add_finding(
                "Medium",
                "Certificate Expiring Soon",
                f"Certificate expires in {ssl['days_remaining']} days.",
                10,
                "Renew the SSL certificate."
            )

    # ---------------- Security Headers ----------------

    headers = modules.get("headers")

    if not headers or "error" in headers:

        add_finding(
            "High",
            "Header Analysis Failed",
            "Unable to retrieve HTTP response headers.",
            10
        )

    else:

        required = headers["headers"]

        header_checks = {

            "Strict-Transport-Security": (
                10,
                "Enable HSTS."
            ),

            "Content-Security-Policy": (
                10,
                "Configure a Content Security Policy."
            ),

            "X-Content-Type-Options": (
                5,
                "Enable X-Content-Type-Options."
            ),

            "Referrer-Policy": (
                3,
                "Configure a Referrer Policy."
            ),

            "Permissions-Policy": (
                3,
                "Configure Permissions Policy."
            )

        }

        for header, (deduction, recommendation) in header_checks.items():

            if not required.get(header):

                add_finding(

                    "Medium",

                    f"{header} Missing",

                    f"{header} header is not configured.",

                    deduction,

                    recommendation

                )

    # ---------------- WHOIS ----------------

    whois = modules.get("whois")

    if whois and "error" not in whois:

        if whois.get("dnssec", "").lower() == "unsigned":

            add_finding(

                "Medium",

                "DNSSEC Disabled",

                "DNSSEC is not enabled.",

                5,

                "Enable DNSSEC."

            )

    # ---------------- DNS ----------------

    dns = modules.get("dns")

    if dns and "error" not in dns:

        if len(dns.get("MX", [])) == 0:

            add_finding(

                "Low",

                "No Mail Server",

                "No MX records were discovered."

            )

        if len(dns.get("TXT", [])) > 15:

            add_finding(

                "Low",

                "Large Number of TXT Records",

                "Review unnecessary TXT records."

            )

    # ---------------- Ports ----------------

    ports = modules.get("ports")

    if ports and "error" not in ports:

        open_ports = list(ports.get("open_ports", {}).keys())

        if 22 in open_ports:

            add_finding(

                "Medium",

                "SSH Exposed",

                "SSH is publicly accessible.",

                5,

                "Restrict SSH access."

            )

        if len(open_ports) > 10:

            add_finding(

                "Medium",

                "Large Attack Surface",

                "Numerous open ports detected.",

                10,

                "Close unnecessary services."

            )

    # ---------------- Subdomains ----------------

    subs = modules.get("subdomains")

    if subs and "error" not in subs:

        total = len(subs.get("subdomains", []))

        if total > 20:

            add_finding(

                "Low",

                "Large Number of Subdomains",

                f"{total} subdomains discovered.",

                5,

                "Review exposed assets."

            )

    # ---------------- Technology ----------------

    tech = modules.get("technology")

    if tech and "error" not in tech:

        technologies = tech.get("technologies", [])

        if "WordPress" in technologies:

            add_finding(

                "Low",

                "WordPress Detected",

                "Ensure WordPress and plugins remain updated."

            )

    # ---------------- Final Score ----------------

    score = max(score, 0)

    if score >= 90:

        severity = "Low"
        grade = "A"

    elif score >= 80:

        severity = "Low"
        grade = "B"

    elif score >= 70:

        severity = "Medium"
        grade = "C"

    elif score >= 50:

        severity = "High"
        grade = "D"

    else:

        severity = "Critical"
        grade = "F"

    return {

        "score": score,

        "grade": grade,

        "severity": severity,

        "findings": findings,

        "recommendations": list(dict.fromkeys(recommendations))

    }