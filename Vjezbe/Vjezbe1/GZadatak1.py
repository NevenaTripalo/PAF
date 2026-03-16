#Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg,
# a program crta x − t, v − t i a −t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji.
#Diferencijalne jednadžbe rješavajte numerički.
#Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import matplotlib.pyplot as plt
import numpy as np

#unos vrijednosti sile i mase
while True:
    sila=input("Unesite zeljeni iznos sile [N]: ")
    try:
        sila=float(sila)
        break
    except:
        print("Čini se da vam se dogodila greska pri unosu. ")
        continue
while True:   
    masa=input("Unesite željenu masu čestice [kg]: ")
    try:
        masa=float(masa)
        if masa>0:
            break
    except:
        print("Čini se da vam se dogodila greska pri unosu. ")
        continue
    
t=10

# a -t graf
#a=F/M kod jednolikog gibanja konstantna
akceleracija=sila/masa
plt.subplot(1, 3, 1)
x=np.linspace(0,t, 10)
y=np.full_like(x,akceleracija)
plt.grid(True)
plt.margins(x=0)
plt.title("Ovisnost akceleracije u vremenu", fontsize=10)
plt.xlabel("vrijeme [s]")
plt.ylabel("akceleracija [m/s^2]")
plt.plot(x,y, color="hotpink")

# v- t graf
#v(t)=v0 + at
while True:
    v0=input("Unesite početnu brzinu čestice [m/s], ako je nema unesite 0: ")
    try:
        v0=float(v0)
        break
    except:
        print("Pogreška pri unosu. ")
        continue
    
#brzina=v0 + akceleracija*t
plt.subplot(1, 3, 2)
x=np.linspace(0, t, 10)
brzina=v0 + akceleracija*x
y=brzina
plt.grid(True)
plt.margins(x=0)
plt.title("Ovisnost brzine u vremenu", fontsize=10)
plt.xlabel("vrijeme [s]")
plt.ylabel("brzina [m/s]")
plt.plot(x,y, color="red")

# x -t graf
#x=x0 + v0t + at^2/2
while True:
    x0=input("Unesite neki početni položaj na x-osi [m] koji tijelo ima: ")
    try:
        x0=float(x0)
        break
    except:
        print("Pogreška pri unosu. ")
        continue

put=x0 + v0 + akceleracija
plt.subplot(1, 3, 3)
x=np.linspace(0, t, 50)
put=x0 + v0 + (akceleracija*x**2)/2
y=put
plt.grid(True)
plt.margins(x=0)
plt.title("Ovisnost puta u vremenu", fontsize=10)
plt.xlabel("vrijeme [s]")
plt.ylabel("put [m]")
plt.plot(x,y, color="blue")

plt.tight_layout()
plt.show()