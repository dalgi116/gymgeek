# Šachovnice
def vytvor_sachovnici():
    sachovnice = []
    for i in range(3):
        sachovnice.append([])
        for policko in range(3):
            sachovnice[i].append(" ")
    return sachovnice
#hraci_plocha = vytvor_sachovnici()

def zobraz_plochu(plocha):
    for radek in plocha:
        print(radek)
#zobraz_plochu(hraci_plocha)

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

# Hra - 1. a 2. hráč
def hra():
    plocha = vytvor_sachovnici()
    hraci = ["X","O"]
    for tah in range(9):
        zobraz_plochu(plocha)
        hrac = hraci [tah %2]
        souradnice = zadej_vstup(plocha, hrac)
        plocha[souradnice[0]][souradnice[1]] = hrac
    zobraz_plochu(plocha)
        

hra()
