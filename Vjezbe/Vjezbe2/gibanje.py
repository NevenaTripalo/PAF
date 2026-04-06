#Koristeći klasu Particle u programu "gibanje.py" kreirajte jednan objekt i postavite ga na neke od vrijednosti
#za koje ste analitički izračunali domet. Da li se numeričko riješenje slaže s analitičkim? Koliko je odstupanje?
from particle import Particle
import math
dt=0.001
cestica1=Particle(v0=40, kut=45, x0=0, y0=0)
cestica1.range(dt)
# analitičko rješenje
v0 = 40
theta = math.radians(45)
g = 9.81
analitički = v0**2 * math.sin(2*theta) / g

print("Numerički domet: ", cestica1.range(dt))
print("Analitički domet:", analitički)
print("Relativna pogreška:", abs(cestica1.range(dt) - analitički) / analitički)