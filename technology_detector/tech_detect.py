import requests


def detect_technology(domain):

    url = "https://" + domain

    technologies = []

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent":"CyberSentinel"
            }
        )

        html = response.text.lower()

        headers = response.headers

        server = headers.get("Server","")

        if server:
            technologies.append(
                "Server : " + server
            )

        powered = headers.get(
            "X-Powered-By"
        )

        if powered:
            technologies.append(
                powered
            )

        checks = {

            "WordPress":"wp-content",

            "Drupal":"drupal",

            "Joomla":"joomla",

            "React":"react",

            "Angular":"angular",

            "Vue.js":"vue",

            "Bootstrap":"bootstrap",

            "jQuery":"jquery",

            "Cloudflare":"cloudflare",

            "Google Analytics":"google-analytics",

            "Hotjar":"hotjar",

            "Express":"express",

            "Next.js":"_next",

            "Nuxt":"_nuxt"

        }

        for tech,pattern in checks.items():

            if pattern in html:

                technologies.append(tech)

        return {

            "domain":domain,

            "technologies":sorted(
                list(set(technologies))
            )

        }

    except Exception as e:

        return {

            "error":str(e)

        }