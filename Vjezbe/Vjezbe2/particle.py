#U zasebnom modulu "particle.py" definirajte klasu Particle za čestice koja će imati
# atribute početne brzine, kuta otklona i koordinata početnog položaja.
#Neka klasa sadrži i sljedeće metode:
#• metodu reset() koja briše sve informacije o čestici
#• privatnu metodu __move() koja pomiče česticu za korak ∆t
#• metodu range() koja numerički računa domet projektila
#• metodu plot_trajectory() koja crta putanju u x - y ravnini za trenutno stanje čestice.

import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, kut, x0, y0):
        self.v0_init = v0
        self.kut_init = (kut) #spremanje pocetnih vrijednosti
        self.x0_init = x0
        self.y0_init = y0
        self.reset()
        
    def reset(self):
        self.v0 = self.v0_init
        self.kut = math.radians(self.kut_init)
        self.x = self.x0_init
        self.y = self.y0_init
        self.vx = self.v0 * math.cos(self.kut)
        self.vy = self.v0 * math.sin(self.kut)
        self.g = 9.81
        self.t = 0
    
    def __move(self, dt): #privatna metoda koja pomice cesticu za dt
        self.t += dt
        self.vy -= self.g*dt  #vy_i+1 = vy_i - gdt
        self.x += self.vx*dt
        self.y += self.vy*dt - 0.5*self.g*dt**2
        # vx_i+1 = vx_i, vx ostaje isti
        
    def range(self, dt): #numericki racuna domet projektila
        self.reset()
        while self.y>=0:
            self.__move(dt)
        return self.x
    
    def plot_trajectory(self, dt): #crta putanju projektila
        self.reset()
        x_koord = []
        y_koord = []
        while self.y>=0:
            x_koord.append(self.x)
            y_koord.append(self.y)
            self.__move(dt)
            
        plt.plot(x_koord, y_koord)
        plt.grid(True)
        plt.title("Putanja cestice")
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()