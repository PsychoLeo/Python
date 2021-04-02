message = 'this if is you not are a reading very this good then way you to have hide done a it message wrong'

# print (dir(message))

words = message.split()
for x in range(0, len(words), 2):
    print('''
''',words[x],)


def read_msg (msg) :
    
    ''' input : a message where half of the words are useless
    output : the message without these useless characters'''
    
    msg_list = msg.split (' ')
    return ' '.join([i for i in msg_list if msg_list.index(i)%2 == 0])
    

print (read_msg (message))