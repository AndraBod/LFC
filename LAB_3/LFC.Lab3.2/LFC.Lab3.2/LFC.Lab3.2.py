def automat_finit_parcare():
    liber = "Liber"
    ocupat = "Ocupat"
    eroare = "Eroare"
    stare = liber  
    locuri = [0] * 5

    while True:
        print("\n    Gestionare Parcare    ")
        print("P - Parcare Mașină")
        print("E - Eliberare Loc")
        print("S - Stare Parcare")
        print("Q - Ieșire\n")

        inp = input("Selectează opțiunea: ").strip().upper()

        if inp == "S":
            status = ''.join(['[X]' if loc else '[ ]' for loc in locuri])
            print(f"Stare parcare: {status}")
        elif inp == "P":
            if 0 not in locuri:
                print("Eroare: Parcarea este plină!")
                stare = eroare
            else:
                loc = locuri.index(0)
                locuri[loc] = 1
                stare = ocupat
                print(f"Mașina a fost parcată la locul {spot + 1}")
        elif inp == "E":
            try:
                loc_nr = int(input("Introdu numărul locului de eliberat: "))
                if loc_nr < 1 or loc_nr > len(locuri):
                    print("Eroare: Loc invalid!")
                    stare = eroare
                elif locuri[loc_nr - 1] == 0:
                    print("Eroare: Locul este deja liber!")
                    stare = eroare
                else:
                    locuri[loc_nr - 1] = 0
                    stare = liber
                    print(f"Mașina a părăsit locul {loc_nr}")
            except ValueError:
                print("Eroare: Introdu un număr valid!")
                stare = eroare
        elif inp == "Q":
            print("Ieșire din sistem.")
            break
        else:
            print("Eroare: Opțiune invalidă!")
            stare = eroare

if __name__ == "__main__":
    automat_finit_parcare()
