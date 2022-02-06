a, b = 2, 1 # L_0, L_1
for i in range (2, 1000) :
	a, b = b, a+b
	if i % 4 == 3 :
		print(b % 4)
