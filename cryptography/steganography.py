from PIL import Image


def encrypt(txt, file):
    global pix_val_flat
    '''input : a text to encrypt and the picture to hide it in
    output : the resultant picture, modified version of the initial'''
    num_rgb = len(txt) * 4
    assert len(pix_val_flat) >= num_rgb, 'Image has not enough pixels'
    lwords = [convert_bin(i) for i in txt]
    lbinrgb_numbers = [convert_num_bin(pix_val_flat[i]) for i in range(num_rgb)]
    # liste de rgb de l'image initiale convertis en binaire
    for i in range(len(lbinrgb_numbers)):
        lbinrgb_numbers[i] = lbinrgb_numbers[i][0:6] + lwords[i // 4][2 * (i % 4):2 * (i % 4) + 2]
    lbinrgb_numbers = [convert_rgb(i) for i in lbinrgb_numbers]
    for i in range(len(lbinrgb_numbers)):
        pix_val[i // 3] = list(pix_val[i // 3])
        pix_val[i // 3][i % 3] = lbinrgb_numbers[i]
        pix_val[i // 3] = tuple(pix_val[i // 3])
    newimg = Image.new(im.mode, im.size)
    newimg.putdata(pix_val)
    filename = input('Enter the file name : ')
    newimg.save(f'/home/leo/Images/autres/steganography/{filename}.png')
    return None


def decrypt(file):
    global pix_val_flat
    '''input : a file to decrypt
    output : the message hidden in the file'''
    decrypted = ''
    pix_val_flat = [convert_num_bin(pix_val_flat[i]) for i in range(len(pix_val_flat))]
    current_binary = ''
    while decrypted[-2:] != ';$':
        for i in range(len(decrypted) * 4, len(decrypted) * 4 + 4):
            current_binary += pix_val_flat[i][-2:]
        decrypted += convert_alph(current_binary)
        current_binary = ''
    print(decrypted[:-2])
    return None


def convert_alph(binary):
    assert len(binary) == 8, 'input is not binary'
    ascii_string = ''
    an_integer = int(binary, 2)
    ascii_character = chr(an_integer)
    return ascii_character


def convert_num_bin(num):
    return bin(num)[2:].zfill(8)


def convert_bin(rgb_str):
    return ''.join(format(i, 'b').zfill(8) for i in bytearray(rgb_str, encoding='utf-8'))


def convert_rgb(bin_str):
    assert len(bin_str) == 8
    res = 0
    for i in range(8):
        res += int(bin_str[i]) * 2**(7 - i)
    return res


if __name__ == '__main__':
    file = input('Enter the file (Images/autres/) : ')
    im = Image.open('/home/leo/Images/autres/' + file, 'r')
    pix_val = list(im.getdata())  # list of all RGB values in the image
    pix_val_flat = [x for sets in pix_val for x in sets]
    mode = input('Enter the mode you want to use (d to decrypt, e to encrypt) : ')
    while mode not in ('e', 'd'):
        print('Invalid input')
        mode = input('Enter the mode you want to use (d to decrypt, e to encrypt) : ')
    if mode == 'e':
        txt = input('Enter the text you want to translate : ')
        encrypt(txt, file)
    else:
        decrypt(file)
