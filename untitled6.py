numero=1
suma_intervalo=0
contador1=0
suma_fuera=0
contador2=0
while True:
    val1=int(input('ingrese el primer valor: '))
    val2=int(input('ingrese el segundo valor: '))
    if val1==val2:
        print('los valores no deben ser iguales')
    else:
        break
if val1>val2:
    minimo=val2
    maximo=val1
else:
    minimo=val1
    maximo=val2
while numero!=0:
    numero=int(input('digite un valor: '))
    if numero>minimo and numero<maximo:
        suma_intervalo+=numero
    elif numero<minimo or numero>maximo:
        suma_fuera+=numero
        contador1+=1
    elif numero==minimo or numero==maximo:
        contador2+=1
    print('la suma de los numeros que estan dentros es: ',suma_intervalo)
    print('el promedio de los numeros que estan fuera es: ',suma_fuera/contador1)
    print('la cantidad de numeros ingresados iguales es a los limites',contador2)
    print('fin del algoritmo')