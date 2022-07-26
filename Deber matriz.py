from random import randint
while True:
    x=int(input("Ingrese la cantidad de filas:"))
    y=int(input("Ingrese la cantidad de columnas:"))
    if x<4 or x>30:
        print("Las filas no pueden ser menores que 4 ni mayores de 30")
    elif y<4 or y>30:
        print("Las columnas no pueden ser menores que 4 ni mayores de 30")
    else:
        break
z=[0]*x

for p in range(x):
    z[p]=[0]*y

for p in range (x):
  for q in range(y):
      n=randint(50,1000)
      z[p][q]=n
for p in range (x):
 for q in range(y):
  print("|",z[p][q],"|",end=" ")
 print("")
print("")

if x==y:
    print("La  principal diagonal es:")


    for p in range (x):
     for q in range(y):
      if p==q:
       print("|",z[p][q],"|",end=" ")
      else:
       print("|","- ","|",end=" ")
     print("")
if x==y:

    print("La segunda diagonal es:")



for p in range (x):
 for q in range(y):
  if p+q==x-1:
   print("|",z[p][q],"|",end=" ")
  else:
   print("|","- ","|",end=" ")
 print("")