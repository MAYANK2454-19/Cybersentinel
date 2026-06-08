def head_parser(banner : str) -> dict[str,str]:
    header = {}
    lines = banner.splitlines()
    for line in lines :
        if ':' in line:
            key,value= line.split(':',1)
            header[key.strip()] = value.strip()
    return header