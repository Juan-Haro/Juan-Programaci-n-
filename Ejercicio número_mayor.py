n=int(input("Ingrese el primer número:"))
n2=int(input("Ingrese el segundo número:"))
n3=int(input("Ingrese el tercer número:"))

def nmayor(n,n2,n3):
    if n>n2 and n2>n3: 
        print("El numero mayor es:",n)
    elif n2>n and n2>n3:
        print("El número mayor es:",n2)
    elif n3>n2 and n3>n:
        print("El número mayor es:",n3)
print(" ")     

nmayor(n, n2, n3)
        