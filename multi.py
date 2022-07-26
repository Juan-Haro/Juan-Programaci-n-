while True: # Define un bucle que se mantiende funcionando mientras la condicion sea verdadera 
    n=int(input("Ingrese el número hasta que tabla desea contar:")) # Define la variable n como un número entero ingresado por teclado
    k=int(input("Ingrese hasta que número quiere multiplicar:")) #Define la variable k como un número entero ingresado por teclado
    if n<2 or n>100 : # Resticción que valida que la variable n no sea menor que 2 ni mayor que 100  
        print("Error , por favor ingrese una tabla de multiplicar del 2 al 100") #Si no se cumple la resticción imprime un mensaje de error y continua el bucle
    if k<1 or k>15:  #Resticción que valida que la variable k no sea menor que 1 ni mayor que 15 
        print("Error , por favor ingrese un número para multiplicar del 1 al 15")  #Si no se cumple la resticción imprime un mensaje de error y continua el bucle
    else:  # Si se cumplen las dos restricciones procede a finalizar el bucle  
      break # Finaliza el bucle
      

   
  
  
  
  
      
      
  