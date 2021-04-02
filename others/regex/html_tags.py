import re


def html_tags(tx, res='all'):
    '''input : html text
    output : either all open tags, close tags or both'''
    if res == 'all':
        all_tags = re.compile(r'</?\w+>')
        return re.findall(all_tags, tx)
    elif res == 'open':
        open_tags = re.compile(r'<[^/][a-zA-Z0-9 ":\./=]*>')
        return re.findall(open_tags, tx)
    elif res == 'close':
        close_tags = re.compile(r'</\w+>')
        return re.findall(close_tags, tx)
    elif res == 'all_tx':
        all_tags_tx = re.compile(r'<.+>')
        return re.findall(all_tags_tx, tx)
    else:
        print('Invalid tag query')
