def latexBoard1D():
    s = "$$\\begin{array}{" + "|c"*mod +"|}\hline\n"
    s += "\\text{a}"
    for i in range (mod) : # construction de la première ligne
        s += f"& {i}"
    s += "\\\\ \hline\n"
    for i in range (mod) :
        s += f" & {getValue([i])%mod} "
    s += "\\\\ \n"
    print(s+"\hline\end{array}$$")

def latexBoard2D():
    s = "$$\\begin{array}{" + "|c"*mod +"|}\hline\n"
    s += "\\text{b\\a}"
    for i in range (mod) : # construction de la première ligne
        s += f"& {i}"
    s += "\\\\ \hline\n"
    for i in range (mod) :
        s += f"{i} "
        for j in range (mod) :
            s += f"& {getValue([i, j])%mod} "
        s += "\\\\ \n"
    print(s+"\hline\end{array}$$")

def getValue(vals) :
    # vals : liste d'entiers [x] ou [x, y] dont on veut calculer f(x) ou f(x, y)
    if len(vals) == 1 :
        return eval(f.replace("a", str(vals[0])))
    fCopy = f.replace("a", str(vals[0]))
    fCopy = fCopy.replace("b", str(vals[1]))
    return eval(fCopy)
        
def getFormattedFunction(f):
    f = f.replace("**", "^")
    f = f.replace("*" ,"\cdot ")
    return f


def getFunction(n) :
    if n == 1 :
        return input("Entrer la fonction f(a) = ")
    return input("Entrer la fonction f(a, b) = ")

def printResult() :
    print()
    print(f"Tableau de congruence de ${ft} \mod {mod}$ :")
    latexBoard1D() if nbVar == 1 else latexBoard2D()

if __name__ == '__main__':
    givenInput = False
    if givenInput :
        mod = int(input("Entrer le modulo : "))
        nbVar = int(input("Entrer le nombre de variables (1 ou 2) : "))
        f = getFunction(nbVar)
    else :
        mod = 7*7*7
        # nbVar = 2
        # f = "(a**2+b**2)*(a+b)**2+(a*b)**2"
        nbVar = 1
        f = "(a**2+1)*(a+1)**2+a**2"
    assert nbVar == 1 or nbVar == 2
    ft = getFormattedFunction(f)
    printResult()