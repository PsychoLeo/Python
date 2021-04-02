import random
import sys

def estimationPi (n) :
	'''
	Input : n (the number of points in the graph) [int]
	Output : an approximation of pi with n points [float]
	'''
	# using the formula pi ~ 4*(points_in_circle/total_points)
	points_in_circle = 0
	for _ in range (n) :
		x, y = random.random(), random.random()
		if x**2 + y**2 <= 1 :
			points_in_circle += 1
	return 4*(points_in_circle/n)

if __name__ == '__main__' :
	print ("Enter the number of points to approximate Pi : ")
	n = int(sys.stdin.readline().strip())
	print (f'Estimation of pi (n={n}) : {estimationPi(n)}')
