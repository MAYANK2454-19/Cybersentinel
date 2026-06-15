import requests


def analyze_headers(domain):

    if not domain.startswith("http"):
        url = f"https://{domain}"
    else:
        url = domain

    try:

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        headers_lower = {
            k.lower(): v
            for k, v in response.headers.items()
        }

        security_headers = {

            "Strict-Transport-Security":
                headers_lower.get(
                    "strict-transport-security"
                ),

            "Content-Security-Policy":
                headers_lower.get(
                    "content-security-policy"
                )
                or
                headers_lower.get(
                    "content-security-policy-report-only"
                ),

            "X-Frame-Options":
                headers_lower.get(
                    "x-frame-options"
                ),

            "X-Content-Type-Options":
                headers_lower.get(
                    "x-content-type-options"
                ),

            "Referrer-Policy":
                headers_lower.get(
                    "referrer-policy"
                ),

            "Permissions-Policy":
                headers_lower.get(
                    "permissions-policy"
                ),

            "Cross-Origin-Opener-Policy":
                headers_lower.get(
                    "cross-origin-opener-policy"
                ),

            "Cross-Origin-Embedder-Policy":
                headers_lower.get(
                    "cross-origin-embedder-policy"
                ),

            "Cross-Origin-Resource-Policy":
                headers_lower.get(
                    "cross-origin-resource-policy"
                ),

            "X-XSS-Protection":
                headers_lower.get(
                    "x-xss-protection"
                )
        }

        score = sum(
            1
            for value in security_headers.values()
            if value
        )

        total_headers = len(security_headers)

        percentage = (
            score / total_headers
        ) * 100

        if percentage >= 90:
            grade = "A"

        elif percentage >= 75:
            grade = "B"

        elif percentage >= 60:
            grade = "C"

        elif percentage >= 40:
            grade = "D"

        else:
            grade = "F"
        print("\n===== FINAL URL =====")
        print(response.url)

        print("\n===== HEADERS =====")

        for k, v in response.headers.items():
            print(k, ":", v)
        return {

            "domain": domain,

            "url": response.url,

            "server":
                response.headers.get(
                    "Server",
                    "Unknown"
                ),

            "status_code":
                response.status_code,

            "score": score,

            "total": total_headers,

            "grade": grade,

            "headers":
                security_headers

        }

    except Exception as e:

        return {
            "error": str(e)
        }