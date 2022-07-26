c=[1,2,3,4,5,6]
i=[1,2,3,4,5,6]
r=[0]*6

for h in range(0,6):
 r[h]=c[h]+i[h]

for h in range (0,6):
 print(r[h], end="  ")
print(" ")
 
for h in range(0,6):
 r[h]=c[h]**i[h]

for h in range (0,6):
 print(r[h], end="  ")
print(" ")

for h in range(0,6):
 r[h]=c[h]-i[h]

for h in range (0,6):
 print(r[h], end="  ") 
print(" ") 
 
for h in range(0,6):
  r[h]=c[h]*i[h]

for h in range (0,6):
  print(r[h], end="  ")
print(" ")  
  
for h in range(0,6):
 r[h]=c[h]/i[h]

for h in range (0,6):
 print(r[h], end="  ")  
print(" ") 