def suite_a (u0,r,n) :
  s = u0
  S = s
  for i in range (n) :
    s += r
    S = S + s
  return "la somme des valeurs est %s et la valeur de u%s est %s " % (S,n,s)

def suite_g (u0,r,n) :
  s = u0
  S = 0
  for i in range (n-1) :
    s = s*r
    S = S + s
  return "la somme des valeurs est %s et la valeur de u%s est %s " % (S,n,s)

def suite_recurrente (u0, n) :
    s = u0
    S = s
    for i in range (n) :
        s = s + 8*n**2 - 42*n + 55 # definition de la suite voulue
        S += s
    return "la somme des valeurs est %s et la valeur de u%s est %s " % (S,n,s)