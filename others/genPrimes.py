# def genPrimes () :
#     yield 2
#     n = 3
#     prime = True
#     while prime :
#         prime = True
#         print ('Entering for loop')
#         for i in range (2, n) :
#             if n % i == 0 :
#                 prime = False
#                 break
#         if prime :
#             yield n
            

def genPrimes () :
    yield 2
    n = 3
    prime = True
    while True :
        prime = True
        for div in range (2, n) :
            if n % div == 0 :
                n += 1
                prime = False
                break
        if prime :
            n += 1
            yield n-1