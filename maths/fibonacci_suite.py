import matplotlib.pyplot as plt

def fibo(n):

  l = [0, 1]
  x = [i for i in range(n)]
  y = []

  for i in range(n):
    s = l[-1] + l[-2]
    l.append(s)
    rapport = l[-1] / l[-2]
    y.append(rapport)

  print(l)
  plt.plot(x, y)
  plt.title('Evolution of the ratio between two consecutive numbers of the Fibonacci suite')
  plt.show()


if __name__ == '__main__':
  n = int(input("Enter the number up to which you want the Fibonacci suite : "))
  fibo(n)
