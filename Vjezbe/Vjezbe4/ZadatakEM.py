#Napišite program koji crta putanju nabijene čestice u konstantnom električnom i magnetnom polju.
# Demonstrirajte valjanost putanje za slučaj nabijene čestice koja se giba u konstatnom magnetnom polju ⃗ B = (0,0,B)
#i ima sve tri komponente početne brzine različite od 0. Kako se u tom slučaju giba elektron, a kako pozitron?
#Prikažite grafove gibanja elektrona i pozitrona za nekoliko kombinacija vrijednosti električnog i magnetskog polja.

import math
import numpy as np
import matplotlib.pyplot as plt

#konstante
m = 9.11e-31
dt = 1e-13

def simulacija(q, E, B):
    v = np.array([1e5, 2e5, 3e5])
    r = np.array([0.0, 0.0, 0.0])

    x_koord=[]
    y_koord=[]
    z_koord=[]

    for i in range(4000):
        x_koord.append(r[0])
        y_koord.append(r[1])
        z_koord.append(r[2])

        F = q * (E + np.cross(v, B))
        a = F / m
        #azurira svaku komponentu vektora v i r
        v = v + a * dt
        #za izračun novog položaja buduća brzina umjesto stare (stabilnije za kruzno gib.)
        r = r + v * dt + 0.5 * a * dt**2

    return x_koord, y_koord, z_koord


# 4 kombinacije polja za demonstraciju i prikaz grafova
# 1) cisto magnetsko
# 2) E djeluje u x smjeru, cikloidni drift
# 3) paralelna polja, E ubrzava q pa se spirala rasteze
# 4) jace B, uza spirala
#naslov, E, B
slucajevi = [("E = (0, 0, 0) B = (0, 0, 1)", np.array([0, 0, 0]), np.array([0, 0, 1])),
    ("E = (1e5, 0, 0) B = (0, 0, 1)", np.array([1e5, 0, 0]), np.array([0, 0, 1])),
    ("E = (0, 0, 1e5) B = (0, 0, 1)", np.array([0, 0, 1e5]), np.array([0, 0, 1])),
    ("E = (0, 0, 0) B = (0, 0, 2)", np.array([0, 0, 0]), np.array([0, 0, 2]))]

# jedna velika slika unutar koje će biti 4 podgrafa
slika = plt.figure(figsize=(12, 10))

# prolazak kroz sve slučajeve i crtanje u 2x2 mrežu
#uzima tupple (tekst i 2 numpy polja) iz slucajevi
# prvo uzima broj slucaja(od 1) i sslucaj
# onda iz slucaja uzima naslov, E i B
for i, (naslov, E_polje, B_polje) in enumerate(slucajevi, start=1):
    
    #pozivanje simulacije 
    x1, y1, z1 = simulacija(-1.602e-19, E_polje, B_polje) # elektron
    x2, y2, z2 = simulacija( 1.602e-19, E_polje, B_polje) # pozitron

    #dodavanje podgrafa na odgovarajuću poziciju (2 retka, 2 stupca, indeks i)
    ax = slika.add_subplot(2, 2, i, projection='3d')

    # crtanje putanja
    ax.plot(x1, y1, z1, label="elektron")
    ax.plot(x2, y2, z2, label="pozitron")

    #postavljanje oznaka i naslova
    ax.set_title(naslov)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.legend()

plt.tight_layout()
plt.show()