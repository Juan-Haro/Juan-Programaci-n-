while True:
    p=int(input("Ingresar un número:"))
    if p<=0:
        print("Los números primos solo pueden ser positivos")
    else:
        break

def np(p):
   
    x=1
    c=0
    while x<=p:
        if p%x==0:
            c+=1
        x+=1 
    if c==2:
        print("El número ",p,"es primo")
    else:
        print("El número ",p," no es primo")    
    
np(p)    