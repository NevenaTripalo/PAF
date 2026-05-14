#Napišite funkciju koja uz#ima broj iteracija N te N puta zbraja 1/3
#pa zatim N puta oduzima 1/3 broju 5.
#Ispišite konačni rezultat za 200, 2000 i 20000 iteracija.
#Objasnite rezultat koji ste dobili.

def zbrajanje(N):
    suma=5
    for i in range(N):
        suma+=(1/3)
    for i in range (N):
        suma-=(1/3)
    return suma

print(zbrajanje(200))
print(zbrajanje(2000))
print(zbrajanje(20000))
