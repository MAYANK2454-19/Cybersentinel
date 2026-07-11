def calculate_risk(report):

    score = 100

    findings = []

    recommendations = []

    modules = report["modules"]

    # ---------------- SSL ----------------

    ssl = modules.get("ssl")

    if ssl and "error" not in ssl:

        if ssl["days_remaining"] < 30:

            score -= 15

            findings.append(
                "SSL certificate expires soon."
            )

            recommendations.append(
                "Renew the SSL certificate."
            )

    # ---------------- Headers ----------------

    headers = modules.get("headers")

    if headers and "error" not in headers:

        required = headers["headers"]

        if not required.get("Strict-Transport-Security"):

            score -= 10

            findings.append(
                "HSTS header missing."
            )

            recommendations.append(
                "Enable HSTS."
            )

        if not required.get("Content-Security-Policy"):

            score -= 10

            findings.append(
                "Content Security Policy missing."
            )

            recommendations.append(
                "Configure CSP."
            )

        if not required.get("X-Content-Type-Options"):

            score -= 5

            findings.append(
                "X-Content-Type-Options missing."
            )

    # ---------------- DNS ----------------

    dns = modules.get("dns")

    if dns and "error" not in dns:

        if len(dns["MX"]) == 0:

            findings.append(
                "No MX records."
            )

    # ---------------- Ports ----------------

    ports = modules.get("ports")

    if ports and "error" not in ports:

        if "open_ports" in ports:

            if 22 in ports["open_ports"]:

                score -= 5

                findings.append(
                    "SSH exposed."
                )

    # ---------------- WHOIS ----------------

    whois = modules.get("whois")

    if whois and "error" not in whois:

        if whois["dnssec"] == "unsigned":

            score -= 5

            findings.append(
                "DNSSEC not enabled."
            )

            recommendations.append(
                "Enable DNSSEC."
            )

    score = max(score, 0)

    if score >= 90:

        severity = "Low"

    elif score >= 70:

        severity = "Medium"

    elif score >= 40:

        severity = "High"

    else:

        severity = "Critical"

    return {

        "score": score,

        "severity": severity,

        "findings": findings,

        "recommendations": recommendations

    }