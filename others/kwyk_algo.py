# def main() :
#     a = 1
#     b = 2
#     while b-a >0.3 :
#         x = (a+b)/2
#         if f(a)*f(x) > 0 : 
#             a = x
#         else :
#             b = x
#     print ((a+b)/2)

# def f(x) :
#     return 3*x**2-11



# def main() :
#     n = 5
#     u = 2400
#     s = 2400
#     for i in range (2, n+1) : # range(2, n) va de 2 à n-1 donc range(2, n+1) va de 2 à n
#         u = 1.5*u
#         s = s+u
#         print (i, u, s)


# def main() :
#     a = 8
#     b = a
#     c = 4*a
#     a = a + 3
#     if b > c:
#         b = a - c
#     else:
#         b = a - b


# def main() :
#     x = 6
#     a = x + 9
#     b = 6*x
#     c = a + b
#     print(c)

# def main():
#     n = 4
#     s = 0
#     for i in range (0, n+1):
#         s = 3+s+i
#         print (i, s)

# def main() :
#     a = 8
#     b = a
#     c = 5*a
#     a = 8*a
#     if b > c:
#         b = a + c
#     else:
#         b = a - b

#     print(b)


# def f(x) :
#     return 2*x**2-10

# def main() :
#     a = 2
#     b = 3
#     while -a + b > 0.3:
#         x = (a + b)/2
#         if f(a)*f(x) > 0:
#             a = x
#         else:
#             b = x
#     print((a + b)/2)

# def main():
#     u = 6400
#     S = 6400

#     n = 5

#     for i in range(2, n + 1):
#         u = 3*u/2
#         S = S + u
#         print(i, u, S)

# def main():
#     S = 0
#     N = 4

#     for i in range(1, N + 1):
#         S = S - i + 2

#     print(S)

def main():
    a = 4
    b = 5*a
    c = a-9
    a = a-8
    if b>c :
        b = a*c
    else :
        b = a+b

main()
