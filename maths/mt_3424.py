def main() :
    MAX = 100
    for i in range (1, MAX): 
        for j in range (1, i) :
            r = ((i+j)**7-i**7-j**7)%mod
            if r == 0 and i % 7 and j % 7 and j+i%7:
                print(i, j)


if __name__ == '__main__':
    mod = 7**7
    main()