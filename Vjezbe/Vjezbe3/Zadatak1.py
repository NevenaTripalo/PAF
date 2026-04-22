#Napišite kod koji sadrži klasu Projectile koja ima implementirane metode za simuliranje kosog hitca u dvije
#dimenzije s otporom zraka. Testirajte za koji korak ∆t Euler-ova metoda daje dovoljno precizno numeričko
#rješenje koje na x − y grafu nema naznake ne-fizikalnog gibanja.

import numpy as np
import math
import matplotlib.pyplot as plt
        
class Projectile:
    def __init__(self, v0, kut, x0, y0, m, r, ro=1.112, Cd=0.5):    #gustoca [kg/m^3], r: polumjer tijela (kugle), C:koef. otpora
        self.v0 = v0
        self.kut = math.radians(kut)
        self.x = x0
        self.y = y0
        self.m = m
        self.ro = ro
        self.r = r
        self.Cd = Cd
        self.A = math.pi * r**2      # površina presjeka
        self.g = 9.81

        # početne brzine
        self.vx = v0 * math.cos(self.kut)
        self.vy = v0 * math.sin(self.kut)
        
        self.t = 0
        
    def SilaOtpora(self, vx, vy):
        v = math.sqrt(vx**2 + vy**2)
        Fo = 0.5 * self.ro * self.Cd * self.A * v**2 # Fo sila otpora zraka
        if v == 0:
            return 0, 0
        # smjer suprotan brzini
        return -Fo * vx / v, -Fo * vy / v #dijelimo vx (vy) sa v da bismo dobili jedinicne vektore brzine za svaku komponentu
            # sila otpora
      
    def korak(self, dt):
        
        Fox, Foy = self.SilaOtpora(self.vx, self.vy)

        ax = Fox / self.m       # akceleracije
        ay = Foy / self.m - self.g

        self.vx += ax * dt      #azuriranje brzina po Euleru
        self.vy += ay * dt

        self.x += self.vx * dt      #azuriranje polozaja po euleru
        self.y += self.vy * dt

        self.t += dt        #azuriranje vremenskog koraka
        
    def hitac(self, dt):
        xs, ys = [self.x], [self.y]     #inicijalizacija varijabli

        while self.y >= 0:
            self.korak(dt)
            xs.append(self.x)
            ys.append(self.y)

        return xs, ys
    
dt_values = [0.1, 0.05, 0.01, 0.005]
for dt in dt_values:
    p = Projectile(v0=50, kut=20, x0=0, y0=0, m=0.2, r=0.05)
    x, y = p.hitac(dt)
    plt.plot(x, y, label=f"dt = {dt}")

plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Usporedba Eulerove metode za različite dt")
plt.legend()
plt.grid()
plt.show()

