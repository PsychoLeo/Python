MAX = 401

def main():
    visited = [False]*MAX
    for a in range (1, MAX) :
        for k in range (2, MAX) :
            for j in range (2, MAX) :
                if a*(1+k+k*j) < MAX :
                    visited[a*(1+k+k*j)] = True
    l = []
    for i in range (MAX) :
        if not visited[i] : l.append(i)

    print(*l)

main()