from random import randint



def Vali(T):
    if T< 4 or T > 30 :
        return False
    else:
        return True and T
def Random(m,T):
 for i in range(T):
    r=randint(10,100)
    m[i]=r
 return m 

def prim(m,f,T):
    c=0
    for j in range(T):
        if m[j]%2!=0 and m[j]%3!=0:
          f.append(v[j])
    return f


while True:
    f= int(input('Ingrese la dimension del vector: '))
       
    Vali(f)
    if Vali(f) ==False:
            print('El valor debe estar dentro del limite de 4 a 30')
            print('\n')
    else:
            break
v=[0]*f    
Random(v,f)
print("El vector original es:")
print("")

for i in range (f):
     print("|",v[i],"|",end="  ")
print("")

p=[]  
prim(v, p,f)
print("")
print("El vector con números primos es: ")
print("")
for i in range (len(p)):
     print("|",p[i],"|",end="  ")   

      
    
               

        
    