#TAJ-szám beolvasása
taj_szam = input("Kérem, adja meg a kilencjegyű TAJ-számot: ")  # Bekéri és eltárolja a kilencjegyű TAJ-számot

#Ellenőrzőszám kinyerése és tárolása
ellenorzo_szam = int(taj_szam[-1])  # Kinyeri és int-ként tárolja az utolsó számot, az ellenőrzőszámot
print("Az ellenőrzőszám:", ellenorzo_szam)  # Kiírja az ellenőrzőszámot

#Szorzatok összegzése
osszeg = 0
for i in range(8):
    szamjegy = int(taj_szam[i])  # Kinyeri az aktuális számjegyet
    if (i + 1) % 2 == 0:  # Páros pozíció
        osszeg += szamjegy * 7  # Héttel szorozza a páros helyen álló számjegyet és hozzáadja az összeghez
    else:  # Páratlan pozíció
        osszeg += szamjegy * 3  # Hárommal szorozza a páratlan helyen álló számjegyet és hozzáadja az összeghez

print("Az összeg értéke:", osszeg)  # Kiírja az összeget

#Ellenőrzés
maradek = osszeg % 10  # Kiszámolja az összeg tízzel vett osztási maradékát
if maradek == ellenorzo_szam:  # Ellenőrzi, hogy az osztási maradék egyezik-e az ellenőrzőszámmal
    print("Helyes a szám!")  # Ha egyezik, kiírja "Helyes a szám!"
else:
    print("Hibás a szám!")  # Ha nem egyezik, kiírja "Hibás a szám!"