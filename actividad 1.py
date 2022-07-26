def l100kmtompg(l):
    m=(100*1000)/1609.344
    g= l/3.785411784
    return m/g

def mpgtol100km(m):
    l=3.785411784
    kil=(m*1609.344)/1000
    k=kil/100 
    return l/k



print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))


print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))