from math import sin, cos, tan, e, pi

def main():
    function = input("f(x) = ")
    left = float(input("Enter the left limit : "))
    right = float(input("Enter the right limit : "))
    print(integral(left, right, function))

def integral(a, b, function) :
    def f(i) :
        return eval(function.replace('x', str(i))) 
    pas = 0.001
    res = 0
    while a < b :
        res += abs(f(a))*pas
        a += pas
    return round(res, 4)

main()