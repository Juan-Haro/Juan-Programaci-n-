def elnumeroesprimo(num):
    contadorprimo = 0
    for i in range(1,num+1):
        if num% i==0:
            contadorprimo+=1
    if contadorprimo==2:
     return True
    else: 
     return False

for o in range(1,20):
     if elnumeroesprimo(o+1):
         print(o+1,end=" ")
         
print()         
            