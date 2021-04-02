# for j in range(803, 1000, 10):
#     for k in range(903, 1000, 10):
#         r = str(j * k)
#         if r[1] == r[-2] and r[0] == r[-1]:
#             print(r)

# c = 0
# for i in range(101):
#     c += i**2

# print(c)

grille = [
    [6, 7, 3, 0, 0, 0, 0, 5, 0],
    [0, 1, 0, 5, 0, 3, 0, 0, 7],
    [9, 2, 5, 6, 0, 0, 0, 8, 0],
    [5, 0, 0, 0, 6, 0, 8, 0, 0],
    [0, 0, 0, 7, 0, 9, 0, 0, 0],
    [0, 0, 7, 0, 1, 0, 0, 0, 6],
    [0, 8, 0, 0, 0, 1, 6, 2, 5],
    [1, 0, 0, 4, 0, 6, 0, 3, 5],
    [0, 3, 0, 0, 0, 0, 1, 4, 8],
]

carreId = (1, 1)
carreId2 = (2, 2)
x, y = carreId2
print([grille[i][j] for i in range(x * 3, x * 3 + 3) for j in range(y * 3, y * 3 + 3)])
