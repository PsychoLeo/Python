def encrypt(msg):
    '''encrypts a message with letters associated
    to its index in alphabet'''
    alph = ' abcdefghijklmnopqrstuvwxyz'  # space included
    numbers = [alph.index(char) for char in msg]
    return ''.join([numberToBinary(i) for i in numbers])


def numberToBinary(number):
    '''input : number (int)
    returns the binary of a letter converted to its
    value associated in encryption'''
    result = ''
    while number > 0:
        result += str(number % 2)
        number //= 2  # trouver number en base 2
    return result[::-1].zfill(5)  # remplir avec des espaces


def binaryToNumber(binary):
    '''returns the binary as a Number (base 2)'''
    total = 0
    for i in range(len(binary)):
        total += 2**(4 - i) * int(binary[i])
    return total


def decrypt(msg):
    '''decrypts a message with letters associated
    to its index in alphabet'''
    alph = ' abcdefghijklmnopqrstuvwxyz'
    assert len(msg) % 5 == 0, 'Message cannot be decrypted'
    msg_split = [msg[x:x + 5] for x in range(0, len(msg), 5)]
    numbers = [binaryToNumber(i) for i in msg_split]
    return ''.join([str(alph[num]) for num in numbers])


if __name__ == '__main__':
    mode = input('Encrypt or decrypt [e/d] : ')
    mode_show = 'encrypt' if mode == 'e' else 'decrypt'
    msg = input(f'Enter the message to {mode_show} : ')
    if mode == 'e':
        print(f'Encrypted message : {encrypt(msg)}')
    else:
        print(f'Decrypted message : {decrypt(msg)}')
