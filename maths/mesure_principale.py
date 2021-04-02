def mesure_principale (a,b) :
    x = a % (2*b)
    if x / b <= -1 :
        x = x + (2*b)
    elif x / b > 1 :
        x = x - (2*b)
    return "La mesure principale de l'angle est %spi/%s" % (x, b)