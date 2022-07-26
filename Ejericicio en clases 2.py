def primo(n):
    c = 0
    for i in range(1,n+1):
        if n% i==0:
            c+=1
    if c==2:
       return True
    else : 
        return False

for k in range(1,20):
     if primo(k+1):
         print(k+1,end=" ")
         
print()         
            