import re


def find_email(txt, mode='mails'):
    sol = []
    pattern = re.compile(r'[\w._+-]+@[a-zA-Z0-0-]+\.[a-zA-Z0-9-.]+')
    for match in re.finditer(pattern, txt):
        if mode == 'mails':
            sol.append(match.group())
        else:
            sol.append((match.start(), match.group()))
    return sol
