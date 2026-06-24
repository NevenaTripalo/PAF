import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#MODEL SUSTAVA (Ishodište y = 0 je na tlu)
class BungeeSustav:
    def __init__(self, m, L0, k, A, Cd, H=100.0, rho=1.225, g=9.81):
        self.m, self.L0, self.k, self.g, self.H = m, L0, k, g, H
        self.cw = 0.5 * rho * Cd * A

    def jednadzba_gibanja(self, y, v, otpor_ukljucen=True):
        """Vraća [brzina, ubrzanje] za trenutno stanje [y, v]."""
        Fg = -self.m * self.g
        
        # uže se rasteže tek kada skakač padne ispod razine (H - L0)
        Fe = self.k * ((self.H - self.L0) - y) if y < (self.H - self.L0) else 0.0
        Fd = -self.cw * v * abs(v) if otpor_ukljucen else 0.0
        
        return np.array([v, (Fg + Fe + Fd) / self.m])

    def pokreni_rk4(self, t_max=40.0, dt=0.01, otpor=True):
        """Računa putanju i sve komponente energije koristeći RK4."""
        t_podaci, stanje_podaci, energije = [], [], []
        stanje = np.array([self.H, 0.0])  # početno stanje: na vrhu litice (y = H), miruje (v = 0)
        t = 0.0

        while t < t_max:
            # RK4 korak integracije
            k1 = self.jednadzba_gibanja(stanje[0], stanje[1], otpor)        # jed gib kao argumente prima visinu, brzinu i boolean za otpor
            k2 = self.jednadzba_gibanja(stanje[0] + 0.5*dt*k1[0], stanje[1] + 0.5*dt*k1[1], otpor)
            k3 = self.jednadzba_gibanja(stanje[0] + 0.5*dt*k2[0], stanje[1] + 0.5*dt*k2[1], otpor)
            k4 = self.jednadzba_gibanja(stanje[0] + dt*k3[0], stanje[1] + dt*k3[1], otpor)
            stanje += (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

            y, v = stanje[0], stanje[1]     #azurirani polozaj i brzina
            
            # izračun energija preko koordinata
            Ek = 0.5 * self.m * v**2
            Epg = self.m * self.g * y
            Eel = 0.5 * self.k * ((self.H - self.L0) - y)**2 if y < (self.H - self.L0) else 0.0
            
            t_podaci.append(t)
            stanje_podaci.append([y, v])
            energije.append([Ek, Epg, Eel])
            t += dt

        return np.array(t_podaci), np.array(stanje_podaci), np.array(energije)


# =====================================================================
# SIMULACIJA 1: ANALIZA ENERGIJE (Standardni skakač, 80 kg)
# =====================================================================
L0_bungee, k_bungee, visina_litice = 30.0, 45.0, 100.0

sustav_std = BungeeSustav(m=80.0, L0=L0_bungee, k=k_bungee, A=0.55, Cd=1.1, H=visina_litice) #kreiramo objekt sustava s parametrima standardnog skakača
t, stanje_bez, e_bez = sustav_std.pokreni_rk4(otpor=False)
_, stanje_s, e_s = sustav_std.pokreni_rk4(otpor=True) #t nam je isti, ne treba ga vracati dva puta

# crtanje energetskih grafova, krecemo s vrha litice i skakac miruje
fig_en, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))        #jedan redak dva stupca, za usporedbu bez i s otporom zraka
# za svaki graf, crtamo kineticku, gravitacijsku i elasticnu energiju te ukupnu energiju
for ax, e, naslov in [(ax1, e_bez, 'Bez otpora zraka (Očuvanje energije)'), (ax2, e_s, 'S kvadratnim otporom (Gubitak energije)')]:
    ax.plot(t, e[:, 0], 'green', label='Kinetička (Ek)')
    ax.plot(t, e[:, 1], 'blue', label='Gravitacijska (Epg)')
    ax.plot(t, e[:, 2], 'orange', label='Elastična (Eel)')
    ax.plot(t, e.sum(axis=1), 'hotpink', linewidth=2, label='UKUPNA ENERGIJA')      #e.sum(axis=1) zbraja sve tri komponente energije po redcima (ukupnu energiju u svakom t)
    ax.set_title(naslov); ax.set_xlabel('Vrijeme (s)'); ax.set_ylabel('Energija (J)'); ax.grid(True); ax.legend()
plt.tight_layout()

# spremljivanje i prikazivanje grafova
plt.savefig('bungee_analiza_energije.png', dpi=300) 
plt.show()
plt.show()


# =====================================================================
# SIMULACIJA 2: USPOREDBA MASA (skakac 60 kg vs skakac 100 kg)
# =====================================================================
# kreiramo dva objekta sustava, jedan za lakog skakača (60 kg) i jedan za teškog skakača (100 kg)
sustav_laki = BungeeSustav(m=60.0, L0=L0_bungee, k=k_bungee, A=0.55, Cd=1.1, H=visina_litice)
sustav_teski = BungeeSustav(m=100.0, L0=L0_bungee, k=k_bungee, A=0.55, Cd=1.1, H=visina_litice)

#vrijeme i energije nam ovdje nisu potrebni, samo nam trebaju putanje (y) i brzine (v) za usporedbu dubine skoka
_, stanje_laki, _ = sustav_laki.pokreni_rk4(otpor=True) # t_max i dt su default vrijednosti, samo dodamo zelimo li otpor zraka ili ne
_, stanje_teski, _ = sustav_teski.pokreni_rk4(otpor=True)

# grafička usporedba putanja različitih masa
plt.figure(figsize=(9, 5))
plt.plot(t, stanje_laki[:, 0], color = 'green', label='Laki skakač (60 kg)')    #uzima se samo visina (y) iz stanja, koje je 2D array [y, v]
plt.plot(t, stanje_teski[:, 0], color='red', label='Teški skakač (100 kg)')
plt.axhline(visina_litice - L0_bungee, color='gray', linestyle='--', alpha=0.7, label='Granica labavog užeta')
plt.axhline(0, color='brown', linestyle='-', linewidth=1.5, label='Tlo (y = 0)')
plt.title('Utjecaj mase skakača na dubinu skoka')
plt.xlabel('Vrijeme (s)'); plt.ylabel('Visina iznad tla y (m)'); plt.legend(); plt.grid(True)
#spremanje slike usporedbe skakaca
plt.savefig('bungee_usporedba_masa.png', dpi=300)
plt.show()


# =====================================================================
# DUPLA ANIMACIJA usporedni skok lakog i teškog skakača 
# =====================================================================
fig_anim, ax_anim = plt.subplots(figsize=(6, 8))
ax_anim.set_xlim(-6, 6)
ax_anim.set_ylim(-5, visina_litice + 5) # Skalirano od podnožja do vrha litice
ax_anim.axhline(visina_litice, color='gray', linewidth=2, label='Platforma')
ax_anim.axhline(0, color='brown', linewidth=2, label='Tlo')
ax_anim.axhline(visina_litice - L0_bungee, color='red', linestyle='--', alpha=0.5, label='Granica užeta')

# elementi za lakog skakača na x = -2
linija_laki, = ax_anim.plot([], [], 'green', linewidth=2, label='Uže (60 kg)')
tocka_laki, = ax_anim.plot([], [], 'go', markersize=10)

# elementi za teškog skakača na x = 2
linija_teski, = ax_anim.plot([], [], color='red', linewidth=2, label='Uže (100 kg)')
tocka_teski, = ax_anim.plot([], [], 'ro', markersize=12)

tekst_vremena = ax_anim.text(-5.5, 5, '', fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
ax_anim.legend(loc='upper right'); ax_anim.grid(True)
ax_anim.set_title('Usporedna Bungee Animacija')
ax_anim.set_ylabel('Visina y (m)')

def init():
    linija_laki.set_data([], [])
    tocka_laki.set_data([], [])
    linija_teski.set_data([], [])
    tocka_teski.set_data([], [])
    tekst_vremena.set_text('')
    return linija_laki, tocka_laki, linija_teski, tocka_teski, tekst_vremena

def animate(i):
    idx = i * 5  # Faktor preskakanja koraka radi glatkoće videa, svaki 5. korak se prikazuje
    if idx >= len(t):       #provjera da nam se ne rusi animacija ako zbog svako 5. premasi broj koraka
        idx = len(t) - 1
    
    y_laki = stanje_laki[idx, 0]
    y_teski = stanje_teski[idx, 0]
    
    # Uže se pruža od vrha litice (visina_litice) prema trenutnoj visini skakača
    linija_laki.set_data([-2, -2], [visina_litice, y_laki])     #horizntalno se ne mijenja pa od -2 do -2
    tocka_laki.set_data([-2], [y_laki])
    
    linija_teski.set_data([2, 2], [visina_litice, y_teski])
    tocka_teski.set_data([2], [y_teski])
    
    tekst_vremena.set_text(
        f'Vrijeme: {t[idx]:.2f} s\n'
        f'Visina Zeleni (60kg): {y_laki:.2f} m\n'
        f'Visina Crveni (100kg): {y_teski:.2f} m'
    )
    return linija_laki, tocka_laki, linija_teski, tocka_teski, tekst_vremena

ani = animation.FuncAnimation(fig_anim, animate, frames=len(t)//5, interval=20, blit=True, init_func=init)

# spremanje animacije kao gif
ani.save('bungee_simulacija.gif', writer='pillow', fps=40)

plt.show()