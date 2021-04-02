import re


def get_filename(path):
    pattern = re.compile(r'\w+\.\w+$')
    matches = re.finditer(pattern, path)
    for match in matches:
        return match.group()
