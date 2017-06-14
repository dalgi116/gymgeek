# Sachovnice
def vytvor_sachovnici():
    sachovnice = []
    for i in range(10):
        sachovnice.append([])
        for policko in range(10):
            sachovnice[i].append(" ")
    return sachovnice

# Hraci plocha
def zobraz_plochu(plocha):
    for radek in plocha:
        print(radek)

# Konec hry
def zkontroluj(plocha, hrac):
    for radek in plocha:
        znaku = 0
        for policko in radek:
            if policko == hrac:
                znaku += 1
            else:
                    znaku = 0
            if znaku == 4:
                return True
    for cislo_sloupce in range(10):
        znaku = 0
        for cislo_radku in range(10):
            if plocha[cislo_radku][cislo_sloupce] == hrac:
                znaku += 1
            else:
                znaku = 0
        if znaku == 4:
            return True
    zleva = 0
    zprava = 0
    for i in range(3):
        if plocha[i][i] == hrac:
            zleva += 1
        else:
            zleva = 0
        if plocha[i][2 - i] == hrac:
            zprava += 1
        else:
            zprava = 0
    if zleva == 4 or zprava == 4:
        return True
    return False
    

# Kontrola podvodu
def zadej_vstup(pole, hrac):
    print("Na tahu je hráč %s."%(hrac))
    vstup = True
    while vstup:
        radek = int(input("Zadej číslo řádku.")) -1
        sloupec = int(input("Zadej číslo sloupce.")) -1
        if 0 <= radek < len(pole[0]) and 0 <= sloupec < len(pole):
            if pole[radek][sloupec].upper() not in ["X","O"]:
                vstup = False
                souradnice = [radek, sloupec]
            else:
                print("Políčko je obsazené.")
        else:
            print("Souřadnice mimo rozsah.")

    return souradnice

# Hra, hraci
def hra():
    plocha = vytvor_sachovnici()
    hraci = ["X","O"]
    tah = 0
    while tah < 100:
        zobraz_plochu(plocha)
        hrac = hraci[tah % 2]
        souradnice = zadej_vstup(plocha, hrac)
        plocha[souradnice[0]][souradnice[1]] = hrac

        if zkontroluj(plocha, hrac):
            break
        
        tah += 1
        
    zobraz_plochu(plocha)
    if tah == 100:
        print("Remíza.")
    else:
        print("Vyhrál hráč {}.".format(hrac))

hra()
