while True:
    p=int(input("Ingresar un n�mero:"))
    if p<=0:
        print("Los n�meros primos solo pueden ser positivos")
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
        print("El n�mero ",p,"es primo")
    else:
        print("El n�mero ",p," no es primo")    
    
np(p)    