import sys
read = lambda : sys.stdin.readline().strip()

numbers = list(range(48, 58))
letters = list(range(65, 91)) + list(range(97, 123))
possible = {i:chr(i) for i in numbers+letters}
print(possible)

def main() :
    scoreGet = int(input())
    findWords(scoreGet)

def findWords(reach, s="", score=0) :
    if score == reach :
        print(s)
    elif score < reach :
        for i in possible: 
            if score+i > reach :
                break
            findWords(reach, s+possible[i], score+i)

def findW (s) :
    score = 0
    for i in s: 
        score += ord(i)
    return score

"""
Pascal : 2o ? (2 octets -> 16 bits)
Carlton : A9 ?
"""

main()