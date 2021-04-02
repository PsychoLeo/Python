import re


def parse_code(tx):
    l = []
    pattern = re.compile(r'[a-zA-z]+')
    for i in re.finditer(pattern, tx):
        l.append(i.group())
    pattern = re.compile(r'[1-9]+')
    for i in re.finditer(pattern, tx):
        l.append(i.group())
    return {'first_name': l[0], 'last_name': l[1], 'id': l[2]}