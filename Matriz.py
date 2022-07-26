f=1
h=1
n=t=0	
while n<=0:
	n=int(input("Ingrese el número de filas "))
while t<=0:
	t=int(input("Ingrese el numero de columnas : "))

while h<=n:
 ñ=int(input("Ingrese los valores de la primera fila:")) 
 h+=1
while f<=t:
 k=int(input("Ingrese los valores de la primera columna:"))  
 f+=1
        
print("   | ",end="\t")
for i in range(1,t+1): 	
 	
 print(f"\t{ñ}",end=" \t ",)
    
print()	

for i in range(1,t*10):  
	print("-",end="")
print()	

for i in range(1,n+1):
 	print("\n",k,"|",end=" \t  ") 
 	for j in range (1,t+1):
	  print(round((ñ*k),1),end=" \t ")