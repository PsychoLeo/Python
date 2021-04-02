c = 0

for i in range(0, 1000):
    if i % 3 and i % 5:
        continue
    else:
        c += i

print(c)
