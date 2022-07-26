while True:
    n=int(input("Ingrese el número hasta que tabla desea contar:"))
    k=int(input("Ingrese hasta que número quiere multiplicar"))
    break

p=0
im=0
m=0
j=0
s=0
h=1
t=1
num=1
while t<=n:
        print("La tabla del ",t," es:")
        while num<=n:
          print(t,"*",num,"=", t*num)    
          num+=1
          
          r=t*num
          s+=r
        t+=1
        num-=n
          
        if r % 3== 0:
              m+=1
          
        if r % 5== 0:
              j+=1
        if r%2==0:
              p+=1
        else:
              im+=1 
          
           
        print("La suma de la tabla del",n,"es:",s)
        print("El promedio es:",s/k)
        print("Los multiplos de 3 son:",m)
        print("Los multiplos de 5 son:",j)
        print("Hay",p,"números pares")
        print("Hay",im,"números impares")
        print("")