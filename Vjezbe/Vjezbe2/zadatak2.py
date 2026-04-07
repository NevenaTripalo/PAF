#Zadatak 2
#Za česticu početne brzine v0 = 10ms i kuta otklona θ = 60o 
# nacrtajte graf ovisnosti relativne pogreške numeričkog riješenja o vrijednosti vremenskog koraka ∆t.
import numpy as np
import matplotlib.pyplot as plt
from particle import Particle
import math

v0 = 10
theta = math.radians(60)
g = 9.81
analiticko = v0**2 * math.sin(2*theta) / g

intervali=np.linspace(0.001, 0.1, 500)
greske = []

for dt in intervali:
    cestica = Particle(10, 60, 0, 0)
    numericko = cestica.range(dt)
    greska = (abs(numericko - analiticko) / analiticko)*100
    greske.append(greska)

plt.plot(intervali, greske)
plt.xlabel("dt [s]")
plt.ylabel("Relativna pogreška [%]")
plt.title("Graf relativne pogreske kosi hitac")
plt.show()