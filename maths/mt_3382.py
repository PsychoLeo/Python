MAX = 301

def main():
    # visited = [False]*MAX
    # for a in range (1, MAX) :
    #     for k in range (2, MAX) :
    #         for j in range (2, MAX) :
    #             n = a*(1+k+k*j)
    #             if n < MAX :
    #                 if n== 18 :
    #                     print(a, k, j)
    #                 visited[n] = True
    # l = []
    # for i in range (MAX) :
    #     if not visited[i] : l.append(i)

    # print(*l)
    valeursPrisesSomme()

def valeursPrisesSomme () :
    visited = [False]*MAX 
    for k in range (2, MAX) :
        for j in range (2, MAX) :
            n = 1+k+k*j
            if n < MAX :
                visited[n] = True
            # for n in range (1+k+k*j, MAX, 1+k+k*j) :
            #     visited[n] = True
            #     if n == 48 :
            #         print(k, j)
    for i in range (MAX) : 
        if visited[i] == False :
            print(i)


main()