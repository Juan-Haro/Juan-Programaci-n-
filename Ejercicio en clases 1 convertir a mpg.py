def l100kmtompg(litros):
    millas=(100*1000)/1609.344
    gallones= litros/3.785411784
    return millas/gallones

def mpgtol100km(millas):
    litros=3.785411784
    kim=(millas*1609.344)/1000
    km=kim/100 
    return litros/km



print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))


print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))