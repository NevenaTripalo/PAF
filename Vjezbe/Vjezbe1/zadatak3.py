#Napišite program koji će korisnika tražiti da upiše (x,y) koordinate za dvije točke. Ako korisnik pogriješi pri likom unosa koordinate opomenite ga da ponovi upis.
# Nakon što je korisnik uspješno upisao dvije koordinate ispišite na ekran jednadžbu pravca koji prolazi kroz te dvije točke.

print("Jednadzba pravca glasi: y=ax+b")
print("Ako unesete kooridnate dviju točaka, program će vratiti jednadžbu toga pravca. ")
koordinate_x=[]
koordinate_y=[]
for i in range (2):
    unos=True
    while unos:
        x=input(f"Unesite x koordinatu za {i+1}. točku: ")
        y=input(f"Unesite y koordinatu za {i+1}. točku: ")
        try:
            x=int(x)
            y=int(y)
        except:
            print("Pokušajte ponovno unijeti koordinatu")
        else:
            koordinate_x.append(x)
            koordinate_y.append(y)
            unos=False
            
x1=koordinate_x[0]
y1=koordinate_y[0]
x2=koordinate_x[1]
y2=koordinate_y[1]
print(f"Koordinate prve točke su {x1, y1}")
print(f"Koordinate druge točke su {x2, y2}")

#rješavanje dvije jednadžbe s dvije nepoznanice (y1=ax1+b, y2=ax2+b)
a=(y1-y2)/(x1-x2)
b=y1-a*x1
print(f"Jednadžba ovoga pravca glasi y={a}x+{b}")
        