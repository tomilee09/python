#este program sirve para calcular el factorial de n con multiprocesamiento
from multiprocessing import Process

def factorial(n):
    """ calcula factorial de n

    n int > 0 """
    if  n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input('dime un numero: '))

#print(factorial(n))

if __name__ == '__main__':
  p = Process(target=factorial, args=(n))
  p.start()
  p.join()