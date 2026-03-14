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
            x=float(x)
            y=float(y)
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

#provjera jesu li točke iste: beskonačno mnogo pravaca
if x1 == x2 and y1 == y2:
    print("Unijeli ste dvije iste točke. Kroz jednu točku prolazi beskonačno mnogo pravaca.")
    exit()

print(f"Koordinate prve točke su {x1, y1}")
print(f"Koordinate druge točke su {x2, y2}")
if x1==x2:
   print(f"Jednadžba ovoga pravca glasi x= {x1}") 
elif y1==y2:
   print(f"Jednadžba ovoga pravca glasi y= {y1}") 
#rješavanje dvije jednadžbe s dvije nepoznanice (y1=ax1+b, y2=ax2+b)
else:
    a=(y1-y2)/(x1-x2)
    a=round(a,2)
    b=y1-a*x1
    b=round(b,2)
    if b<0:
        print(f"Jednadžba ovoga pravca glasi y={a}x {b}")
    else:
        print(f"Jednadžba ovoga pravca glasi y={a}x+{b}")
        