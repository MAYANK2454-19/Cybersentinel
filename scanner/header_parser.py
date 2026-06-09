def head_parser(banner: str) -> dict:
    headers = {}

    if not banner:
        return headers

    for line in banner.splitlines():

        if ":" in line:

            key, value = line.split(":", 1)

            headers[key.strip().lower()] = value.strip()

    return headers