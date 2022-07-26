from random import randint
while True:
 filas=int(input("Ingrese el número de filas:"))
 colum=int(input ("Ingrese el número de columnas:"))
 print("")
 if filas<4 or filas>30:
        print("Las filas deben ser menores que 30 y mayores que 4")
        
 elif colum<4 or colum>30:
         print("Las columnas deben ser menores que 30 y mayores que 4")
         
 else:
     break 
 
     
vector=[0]*filas
for i in range(filas):
    vector[i]=[0]*colum

for j in range (filas):
   for k in range (colum):
    t=randint(0,1000)
    vector[j][k]=t  

for h in range (filas):
   for y in range (colum):
       print(vector[h][y],end="  ")
   print("")   

print(" ")
nmayor=0
for g in range(filas):
    for t in range(colum):
        if vector[g][t]>nmayor:
            nmayor=vector[g][t]
            f=g
            c=t
print("El número",vector[f][c],"es el mayor y se encuentra en la posición[",f,"]""[",c,"]")    

                
            
        
        

    
    

       


              