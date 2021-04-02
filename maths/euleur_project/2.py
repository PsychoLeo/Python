a, b = 1, 1
total = 0

while b < 4000000:
    a, b = b, a + b
    if a % 2 == 0:
        total += a

print(total)
