#Cálculo del salario
#Nombre: Juan Haro

print("Cálculo del salario ")
nombre=input("Ingrese su nombre: ")
horas=int(input("Ingrese las horas: "))
precio=int(input("Ingrese el precio: "))
bruto=horas*precio
tasas=0.25*bruto
neto=bruto-tasas
print("El salario bruto es: ",bruto)
print("Las tasas son : ",tasas)
print("El salario neto es: ",neto)


