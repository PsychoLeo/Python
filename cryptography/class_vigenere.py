from string import ascii_lowercase
alph = ascii_lowercase

class Vigenere:

    # defining initialization function

    def __init__(self, txt, key, mode='e'):
        self.txt = txt
        self.key = key
        self.mode = mode

    # encrypting / decrypting function

    def translate(self):

        ltxt = list(self.txt.lower())
        repeated_key = list((len(self.txt) // len(self.key)) * self.key + self.key[:len(self.txt) % len(self.key)])
        assert len(ltxt) == len(repeated_key), 'text and repeated key are not same length'

        if self.mode == 'e':
            decrypted = []
            for i in range(len(ltxt)):
                if ltxt[i].lower() in alph:
                    decrypted.append(alph[(alph.index(ltxt[i]) + alph.index(repeated_key[i])) % 25])
                else:
                    decrypted.append(ltxt[i])
            return ''.join(decrypted)
        elif self.mode == 'd':
            encrypted = []
            for i in range(len(ltxt)):
                if ltxt[i].lower() in alph:
                    encrypted.append(alph[(alph.index(ltxt[i]) - alph.index(repeated_key[i])) % 25])
                else:
                    encrypted.append(ltxt[i])
            return ''.join(encrypted)

        else:
            print('Invalid mode')

    # defining 3 setter functions

    def set_mode(self, new_mode):
        self.mode = new_mode
        return None

    def set_key(self, new_key):
        self.key = new_key
        return None

    def set_text(self, new_text):
        self.txt = new_text
        return None

    # defining 3 getter functions

    def get_text(self):
        return self.txt

    def get_key(self):
        return self.key

    # get_text = lambda self : self.text
    # get_key = lambda self : self.key

    def get_mode(self):
        if self.mode == 'e':
            return 'Encrypting'
        elif self.mode == 'd':
            return 'decrypting'
        else:
            return 'Invalid mode'
