from random import randint

while True:
 N=int(input("Ingrese el número de filas:"))

 if N<4 or N>30:
  print("Las filas no pueden ser menores que 4 ni mayores de 30")
 else:
  break
while True:

 M=int(input ("Ingrese el número de columnas:"))
 if M<4 or M>30:
  print("Las columnas no pueden ser menores que 4 ni mayores de 30")
 else:
  break

m=[0]*N

for i in range(N):
  m[i]=[0]*M

for i in range (N):
 for j in range(M):
  h=randint(50,1000)
  m[i][j]=h

print("")
print("La matriz es :")
print("")
for i in range (N):
 for j in range(M):
  print("|",m[i][j],"|",end=" ")
 print("")
print("")

if N==M:
 print("La diagonal principal es:")
 print("")

 for i in range (N):
  for j in range(M):
   if i==j:
    print("|",m[i][j],"|",end=" ")
   else:
    print("|","-  ","|",end=" ")
  print("")
print("")  
if N==M:

 print("La diagonal secundaria es:")
 print("")
for i in range (N):
 for j in range(M):
  if i+j==N-1:
   print("|",m[i][j],"|",end=" ")
  else:
   print("|","-  ","|",end=" ")
 print("")
