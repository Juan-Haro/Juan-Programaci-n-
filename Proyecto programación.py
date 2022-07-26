from sympy import *
from time import sleep
lis=["Bienvenido a la calculadora de integrales por tabla","Para realizar una integral indefinida ingrese 1","Para realizar una integral definida ingrese 2"]
def im():
    x=symbols("x")
    f=input("Ingrese la función f=")
    respuesta=integrate(f,x)
    return print("La integral es:",respuesta,"+C")
def ip():

    k=input("Ingrese la función f=")
    x=symbols("x")
    ls=input("Ingrese el limite superior:")
    li=input("Ingrese el limite inferior:")
    respuesta=integrate(k,(x,li,ls))
    return print("La integral es:",respuesta)
for i in range(3):
    print("[",lis[i],"]")
    print("")
    sleep(2)
while True:
    while True:
        dd=input("Ingrese su opción:")
        print("")
        if dd=="1":
            sleep(1)
            print("Ha elegido hacer una integral indefinida")
            
            break
        
        elif dd=="2":    
            sleep(1)
            print("Ha elegido hacer una integral definida")
            
            break
        else:
            print("Error , ingrese nuevamente una opción correcta")
    
    sleep(1)
    if dd=="1": 
        im()
        
    if dd=="2":    
        ip()
    sleep(1)    
    c=input("Si desea realizar otra integral digite cualquier tecla , en caso contrario digite la letra S :") 
    print("")
    if c=="S" or c=="s":
        sleep(1)
        print("Espero que el programa le haya servido")
        print("")
        sleep(1)
        print("Vuelva proto :3")
        break
        