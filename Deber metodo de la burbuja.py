from random import randint
from time import sleep
def ordenar(az):
    l=len(az)-1
    for u in range (0,l):
        for j in range (0,l):
            if az[j]>az[j+1]:
             au=az[j]
             az[j]=az[j+1]
             az[j+1]=au
            
    return az            

while True:
 n=int(input("Ingrese el tamaño del vector:"))
 if n<0:
  print("El arreglo debe ser mayor de 1")  
 else:
  break   
L=[0]*n

for h in range(0,n):
    i=randint(50,100)
    L[h]=i
  
print("Los valores antes de ser ordenados son:")
 
for h in range(0,n):
    sleep(1) 
    print(" El valor en la posición",h+1,"es:", L[h])
print("")      
print("Dando el vector :")
for h in range(0,n):
    sleep(1) 
    print("", L[h],end="  ")
print("")        

sleep(1) 
print("") 
print("Los valores ordenados son :")
print("") 
ordenar(L)   
for y in range(0,n):
    sleep(1) 
    print( "El vector ordenado en la posición",y+1,"es:",L[y])
print("")        

print("Dando el vector :")
for y in range(0,n):
     sleep(1) 
     print("", L[y],end="  ")
print("")      