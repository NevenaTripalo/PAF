#Napišite program koji crta putanju nabijene čestice u konstantnom električnom i magnetnom polju.
# Demonstrirajte valjanost putanje za slučaj nabijene čestice koja se giba u konstatnom magnetnom polju ⃗ B = (0,0,B)
#i ima sve tri komponente početne brzine različite od 0. Kako se u tom slučaju giba elektron, a kako pozitron?
#Prikažite grafove gibanja elektrona i pozitrona za nekoliko kombinacija vrijednosti električnog i magnetskog polja.

import math
import numpy as np
import matplotlib.pyplot as plt

m = 9.11e-31
B = np.array([0, 0, 1])
E = np.array([0, 0, 0])

dt = 1e-13

def simulacija(q):
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

        v = v + a * dt
        r = r + v * dt

    return x_koord, y_koord, z_koord

# elektron i pozitron
x1, y1, z1 = simulacija(-1.6e-19)
x2, y2, z2 = simulacija( 1.6e-19)

# crtanje
slika = plt.figure()
ax = slika.add_subplot(projection='3d')

ax.plot(x1, y1, z1, label="elektron")
ax.plot(x2, y2, z2, label="pozitron")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.legend()
plt.show()