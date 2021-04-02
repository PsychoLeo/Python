def drange(*args):
    '''input : 1,2,3 arguments like in range, but step can be floating
    output : a range using folating point numbers'''

    dec = []
    for i in args:
        if '.' in str(i):
            dec.append(len(str(i).split('.')[1]))
    dec = max(dec) if dec != [] else 0

    assert len(args) <= 3 and len(args) > 0, 'Expected number of arguments : 1,2,3 | Given : %s' % len(args)
    result = []

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

print (drange (1, 10, 0.2))