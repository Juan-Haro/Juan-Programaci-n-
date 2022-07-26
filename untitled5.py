s=0 #Acumulador que guarda los números ingresados dentro del intervalo
p=0 #Contador de las veces que se ha ingresado un número fuera del intervalo
p2=0 #Contador de las veces que se ingreso un número igual al intervalo
s2=0 #Acumulador que guarda los números ingresados fuera del intervalo
while True: # Bucle que permite la repetición mientras cumpla la condición de ser verdadero
    a=int(input("ingrese el primer valor: ")) #Define la primera variable por teclado
    b=int(input("Ingrese el segundo valor: ")) #Define la segunda variable por teclado
    if a==b: # Valida que las variables no sean iguales
        print("Los números no pueden ser iguales") #Imprime en caso de que se de la condición
    else:   #si no se cumple la condición el bucle termina
        break
if a<b: # Da una condicion para validar el limite inferior y superior
    min=a
    max=b
else:  # Si no se cumple la condición valida de diferente forma los limites
    min=b
    max=a
while True: # Bucle que permite la repetición mientras cumpla la condición de ser verdadero
    c=int(input("Ingrese un valor: ")) # Define una variable por teclado
    if c==0: # Valida que la variable no sea 0 y si es 0 termina el programa
        break
    elif min<c and max>c: #Valida que la variable este dentro de los limites 
        s+=c #Si cumple la condición suma los valores dentro de los limites
    elif min>c or max<c:  #Valida que la variable este fuera de los limites 
        s2+=c #Si cumple la condicion suma los valores fuera de los limites
        p+=1  #Cuenta el número de valores ingresados fuera de los limites 
    elif min==c or max==c: #Valida si la variable es igual a los limites
        p2+=1 #Si cumple la condicion cuenta los números ingresados que son iguales a los limites 
        
print("La suma es:",s)  #Imprime la suma de los números dentro del los limites      
print("El promedio es :",s2/p) #Imprime el promedio de los números fuera de los limites    
print("La cantidad de números iguales a los limites son: ",p2) #Imprime el número de valores ingresados iguales a los limites
print("Fin del programa") #Imprime el fin del programa


