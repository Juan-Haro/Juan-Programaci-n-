import random
import time

def Burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):
        for j in range(n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                
 
n=int(input('Ingrese el tamaño del vector: '))
Vector = [0]*n
for i in range (n):
    V=(random.randint(50, 100))
    Vector[i]=V
print("El vector original es :")
print(Vector) 
time.sleep(1)
Burbuja(Vector)
print('El vector oredenado es:')
print(Vector)
