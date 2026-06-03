#Napišite program linregress.py za određivanje modula torzije Dt aluminijske šipke ako znamo da vrijedi
#M=Dt·φ.
#Parametri su nam zadani kao M = [0.052,0.124,0.168,0.236,0.284,0.336] Nm, φ = [0.1745,0.3491,0.5236,0.6981,0.8727,1.0472] rad

import math
import matplotlib.pyplot as plt

# parametri
M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]      # y
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]  # x

n = len(M)

#racunamo sumu xy
suma_xy = 0
for i in range(n):
    x = phi[i]
    y = M[i]
    suma_xy += x * y

#racunamo sumu x^2
suma_x2 = 0
for i in range(n):
    x = phi[i]
    suma_x2 += x * x

# raacunamo sumu y^2
suma_y2 = 0
for i in range(n):
    y = M[i]
    suma_y2 += y * y

#srednje vrijednosti
xy_srednje = suma_xy / n
x2_srednje = suma_x2 / n
y2_srednje = suma_y2 / n

#racunamo nagib pravca a, iz formule se vidi da je to torzijski modul
a = xy_srednje / x2_srednje

#pogreška nagiba sigma
sigma_a = math.sqrt((1/n) * (y2_srednje / x2_srednje - a*a))

# 7. Ispis
print("D_t (modul torzije) =", a)
print("sigma_a =", sigma_a)

plt.title("Linearna regresija: M = Dt*fi")
plt.xlabel("phi [rad]")
plt.ylabel("M[Nm]")
plt.scatter(phi,M)

x=phi
y=[a* x for x in x]

plt.plot(x,y, color="hotpink", label="Model M= Dt * fi")
plt.grid()
plt.show()