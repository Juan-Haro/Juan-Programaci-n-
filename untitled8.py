while True:
    n=int(input("Ingrese el número hasta que tabla desea contar:")) 
    k=int(input("Ingrese hasta que número quiere multiplicar:")) 
    if n<2 or n>100 :
        print("Error , por favor ingrese una tabla de multiplicar del 2 al 100")
    if k<1 or k>15:
        print("Error , por favor ingrese un número para multiplicar del 1 al 15")  #Si no se cumple la resticción imprime un mensaje de error y continua el bucle
    else:  # Si se cumplen las dos restricciones procede a finalizar el bucle  
      break # Finaliza el bucle
p=0  #Define un contador para los nímeros pares 
im=0 #Define un contador para los números impares 
m=0  #Define un contador para los multiplos de 3
j=0  #Define un contador para los multiplos de 5
s=0  #Define un acumulador para las suma 
for h in range(1,n+1): #Establece un bucle con la variable h en un rango de 1 hasta n+1
      s=0 #Se encera el acumulador de la suma
      m=0 #Se encera el contador de los multiplos de 3
      j=0 #Se encera el contador de los multiplos de 5
      p=0 #Se encera el contador de los números pares
      im=0 #Se encera el contador de los números impares
      print("La tabla del ",h," es:") #Imprime la tabla que se va a realizar 
      for i in range(1,k+1): #Establece un bucle con la variable i en un rango de 1 hasta k+1
          r=h*i #Define que la variable r es igual a la multiplicación de h por i
          s+=r # Se van sumando los resultados de la multiplicación en el acumulador de suma 
          if r % 3== 0: #resticción que valida que el módulo de la divición para 3 sea igual a 0
              m+=1 #Si se cumple la condición suma 1 al contador de multiplos de 3
          if r % 5== 0: #resticción que valida que el módulo de la divición para 5 sea igual a 0
              j+=1 #Si se cumple la condición suma 1 al contador de multiplos de 5
          if r%2==0: #resticción que valida que el módulo de la divición para 2 sea igual a 0
              p+=1 #Si se cumple la condición suma 1 al contador de pares
          else: # Resticcion que valida si la resticcion anterior no se cumple 
              im+=1 #Si la resticcion anterior no se cumple suma 1 al contador de impares
          print(h,"*",i,"=", r) #Imprime la multiplicación y el resultado 
      print("La suma de la tabla del",h,"es:",s) #Imprime la suma de cada tabla de multiplicar
      print("El promedio es:",s/k) #Imprime el promedio de la suma de cada tabla de multiplicar
      print("Los múltiplos de 3 son:",m) #Imprime cuantos múltiplos de 3 hay en cada tabla de multiplicar
      print("Los múltiplos de 5 son:",j) #Imprime cuantos múltiplos de 5 hay en cada tabla de multiplicar
      print("Hay",p,"números pares") #Imprime cuantos números pares hay en cada tabla de multiplicar
      print("Hay",im,"números impares") #Imprime cuantos números impares hay en cada tabla de multiplicar
      print("") #Imprime un espacio vacio
      
                      
           
         