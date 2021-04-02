def encrypt(word):
    wd_list = [i for i in word]
    wd_list.reverse ()
    changes = {'a':'0', 'e':'1', 'i':'2', 'o':'2', 'u':'3'}
    for i in range (len(wd_list)) :
        wd_list[i] = changes.get (wd_list[i], wd_list[i])
    return ''.join (wd_list) + 'aca'