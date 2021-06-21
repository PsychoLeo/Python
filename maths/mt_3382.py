MAX = 301

def main():
    visited = [False]*MAX
    for a in range (1, MAX) :
        for k in range (2, MAX) :
            for j in range (2, MAX) :
                n = a*(1+k+k*j)
                if n < MAX :
                    if n== 18 :
                        print(a, k, j)
                    visited[n] = True
    l = []
    for i in range (MAX) :
        if not visited[i] : l.append(i)

    print(*l)

main()