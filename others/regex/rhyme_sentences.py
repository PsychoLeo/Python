def does_rhyme(s1, s2):
    w1 = s1.split(' ')[-1].lower()
    w2 = s2.split(' ')[-1].lower()
    return all([w1.count(i) == w2.count(i) for i in 'aeiou'])

# move to another folder