while True: # Define un bucle que se mantiende funcionando mientras la condicion sea verdadera 
    n=int(input("Ingrese el n�mero hasta que tabla desea contar:")) # Define la variable n como un n�mero entero ingresado por teclado
    k=int(input("Ingrese hasta que n�mero quiere multiplicar:")) #Define la variable k como un n�mero entero ingresado por teclado
    if n<2 or n>100 : # Resticci�n que valida que la variable n no sea menor que 2 ni mayor que 100  
        print("Error , por favor ingrese una tabla de multiplicar del 2 al 100") #Si no se cumple la resticci�n imprime un mensaje de error y continua el bucle
    if k<1 or k>15:  #Resticci�n que valida que la variable k no sea menor que 1 ni mayor que 15 
        print("Error , por favor ingrese un n�mero para multiplicar del 1 al 15")  #Si no se cumple la resticci�n imprime un mensaje de error y continua el bucle
    else:  # Si se cumplen las dos restricciones procede a finalizar el bucle  
      break # Finaliza el bucle
      

   
  
  
  
  
      
      
  