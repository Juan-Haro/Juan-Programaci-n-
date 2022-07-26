np=int(input("Ingrese cualquier número:"))
def npal(np):
    y=str(np)
    x=y[::-1]
    if y==x:
      print("EL número ingresado es palíndromo")
    else:
      print("El número ingresado no es palíndromo")
npal(np)