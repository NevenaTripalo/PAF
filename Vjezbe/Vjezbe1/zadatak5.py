# Unaprijedite kod iz prethodnog zadatka koristeći modul matplotlib.pyplot 
# tako da nacrtate unesene koordinate i pravac koji prolazi kroz njih.
# Ponudite u funkciji opciju da se graf prikaže na ekranu ili da se spremi kao PDF.
# Dopustite korisniku da bira ime pod kojim će se spremiti graf.

import matplotlib.pyplot as plt
import numpy as np 

def pravac(par1, par2):
    x1, y1=par1
    x2, y2=par2
#provjera jesu li točke iste: beskonačno mnogo pravaca
    if x1 == x2 and y1 == y2:
        print("Unijeli ste dvije iste točke. Kroz jednu točku prolazi beskonačno mnogo pravaca.")
        naslov= f"točka({x1}, {y1})"
        return "tocka", naslov, None, None

    elif x1==x2:
        print (f"Jednadžba ovoga pravca glasi x= {x1}")
        naslov=f"x= {x1}"
        return "vertikala", naslov, None, None
    elif y1==y2:
        print (f"Jednadžba ovoga pravca glasi y= {y1}")
        y=y1
        naslov = f"y={y1}"
        return "horizontala", naslov, 0, y
    #rješavanje dvije jednadžbe s dvije nepoznanice (y1=ax1+b, y2=ax2+b)
    else:
        a=(y1-y2)/(x1-x2)
        a=round(a,2)
        b=y1-a*x1
        b=round(b,2)
        if b<0:
            print (f"Jednadžba ovoga pravca glasi y={a}x{b}")
            naslov= f"y={a}x{b}"
        else:
            print (f"Jednadžba ovoga pravca glasi y={a}x+{b}")
            naslov= f"y={a}x+{b}"
        
        return "kosina", naslov, a, b
        
def crtanje(par1, par2):
    x1, y1=par1
    x2, y2=par2

    slucaj, naslov, a, b = pravac(par1, par2)
    
    if (slucaj == "vertikala" and y2 < y1) or (x2 < x1):
        x1, x2= x2, x1
        y1, y2= y2, y1    
            
    while True:
        odabir=input("Želite li prikazati graf u prozoru (upišite:'SHOW') ili ga spremiti kao pdf (upišite'PDF')").upper()
        if odabir=="SHOW":
            naredba=plt.show
            break
        elif odabir=="PDF":
            ime=input("Pod kojim naslovom želite spremiti graf? ")
            naredba=lambda: plt.savefig(f"{ime}.pdf") #ne izvršava se odmah a moze imat argument
            break
        else:
            print("Pokušajte ponovno. ")
            continue
            
    plt.title(naslov)
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x1, y1, marker="o", markersize=10)
    plt.plot(x2, y2, marker="o", markersize=10)
    
    # Za opciju 'tocka', tocka je vec iscrtana
        
    if slucaj=="vertikala":
        y=np.linspace(y1-2,y2+2, 20)
        x=np.full_like(y, x1)
        plt.plot(x,y)
        
    elif slucaj=="horizontala":
        x=np.linspace(x1-2,x2+2,20)
        y=a*x+b
        plt.plot(x,y)
        
    elif slucaj=="kosina":
        x=np.linspace(x1-2,x2+2,20)
        y=a*x+b
        plt.plot(x,y)
    
    naredba()    

crtanje((7,8), (1,2))