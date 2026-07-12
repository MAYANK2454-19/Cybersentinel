import requests
import re


def validate_domain(domain):

    domain = domain.strip().lower()

    pattern = r"^(?!-)(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,}$"

    if not re.match(pattern, domain):

        raise Exception(
            "Please enter a valid domain name."
        )

    return domain


def analyze_headers(domain):

    domain = validate_domain(domain)

    url = f"https://{domain}"

    try:

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent":
                "CyberSentinel/1.0"
            }
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

        percentage = (score / total_headers) * 100

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

            "score":
                score,

            "total":
                total_headers,

            "grade":
                grade,

            "headers":
                security_headers

        }

    except requests.exceptions.SSLError:

        raise Exception(
            "The target does not support a valid HTTPS connection."
        )

    except requests.exceptions.ConnectTimeout:

        raise Exception(
            "Connection timed out while retrieving HTTP headers."
        )

    except requests.exceptions.ConnectionError:

        raise Exception(
            "Unable to connect to the target server."
        )

    except requests.exceptions.InvalidURL:

        raise Exception(
            "Invalid URL supplied."
        )

    except Exception as e:

        raise Exception(
            f"Security Header Analysis failed: {e}"
        )


if __name__ == "__main__":

    print(
        analyze_headers("google.com")
    )