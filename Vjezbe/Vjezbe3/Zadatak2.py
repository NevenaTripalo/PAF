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
        
        self.x0 = x0        #ako pozovemo za isti objekt vise puta hitac
        self.y0 = y0

        # početne brzine
        self.vx = v0 * math.cos(self.kut)
        self.vy = v0 * math.sin(self.kut)
        
        self.t = 0
        
    def SilaOtpora(self, vx, vy):
        v = math.sqrt(vx**2 + vy**2)
        if v == 0:
            return 0, 0
        Fo = 0.5 * self.ro * self.Cd * self.A * v**2 # Fo sila otpora zraka
        # smjer suprotan brzini
        return -Fo * vx/v, -Fo * vy/v #dijelimo vx (vy) sa v da bismo dobili jedinicne vektore brzine za svaku komponentu
    
    def akceleracije(self, vx, vy): #funkcija nam treba za runge kuttu, za elulera moze biti samo definirano 
        Fox, Foy = self.SilaOtpora(vx, vy)
        ax = Fox / self.m
        ay = Foy / self.m - self.g
        return ax, ay

      
    def korak_E(self, dt):
       
        ax, ay = self.akceleracije(self.vx, self.vy)
        
        self.x += self.vx * dt      #azuriranje polozaja po euleru
        self.y += self.vy * dt

        self.vx += ax * dt      #azuriranje brzina po Euleru
        self.vy += ay * dt

        self.t += dt        #azuriranje vremenskog koraka
        
    def korak_rk4(self, dt):

        # --- k1 ---
        k1x = self.vx
        k1y = self.vy
        k1vx, k1vy = self.akceleracije(self.vx, self.vy)

        # --- k2 ---
        vx2 = self.vx + 0.5 * dt * k1vx
        vy2 = self.vy + 0.5 * dt * k1vy
        k2x = vx2
        k2y = vy2
        k2vx, k2vy = self.akceleracije(vx2, vy2)

        # --- k3 ---
        vx3 = self.vx + 0.5 * dt * k2vx
        vy3 = self.vy + 0.5 * dt * k2vy
        k3x = vx3
        k3y = vy3
        k3vx, k3vy = self.akceleracije(vx3, vy3)

        # --- k4 ---
        vx4 = self.vx + dt * k3vx
        vy4 = self.vy + dt * k3vy
        k4x = vx4
        k4y = vy4
        k4vx, k4vy = self.akceleracije(vx4, vy4)

        # --- update položaja i brzine ---
        self.x  += (dt/6) * (k1x  + 2*k2x  + 2*k3x  + k4x)
        self.y  += (dt/6) * (k1y  + 2*k2y  + 2*k3y  + k4y)
        self.vx += (dt/6) * (k1vx + 2*k2vx + 2*k3vx + k4vx)
        self.vy += (dt/6) * (k1vy + 2*k2vy + 2*k3vy + k4vy)

        self.t += dt

    def hitac(self, dt, metoda="euler"):
        self.x, self.y = self.x0, self.y0 #resetiranje varijabli
        self.vx = self.v0 * math.cos(self.kut)
        self.vy = self.v0 * math.sin(self.kut)
        self.t = 0
        xs, ys = [self.x], [self.y]     #inicijalizacija varijabli

        while self.y >= 0:
            if metoda == "euler":
                self.korak_E(dt)
            else:
                self.korak_rk4(dt)

            xs.append(self.x)
            ys.append(self.y)

        return xs, ys
    
dt=0.01
p = Projectile(v0=50, kut=20, x0=0, y0=0, m=0.6, r=0.05)
x_e, y_e = p.hitac(dt, metoda="euler")
x_rk, y_rk = p.hitac(dt, metoda="rk4")

plt.plot(x_e, y_e, label="Euler", linewidth=2)
plt.plot(x_rk, y_rk, label="Runge-Kutta 4", linestyle="--", linewidth=2)

plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Usporedba Euler i Runge-Kutta metode (dt = 0.01)")
plt.legend()
plt.grid()
plt.show()