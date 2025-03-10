def automat_finit():
    q0 = "q0"
    q1 = "q1"
    q2 = "q2"
    q3 = "q3"
    q4 = "q4"
    q5 = "q5"
    stare = q0  
    comanda_confirmata = False  
    bautura_selectata = None  

    while True:
        print("\n    Meniu Băuturi    ")
        print("C - Cafea")
        print("T - Ceai")
        print("A - Cappuccino")
        print("H - Ciocolată caldă")
        print("O - Confirmare comandă")
        print("D - Anulează comanda\n")

        inp = input("Selectează băutura: ").strip().upper()

        if inp == "C":
            stare = q1
            bautura_selectata = "Cafeaua"
        elif inp == "T":
            stare = q2
            bautura_selectata = "Ceaiul"
        elif inp == "A":
            stare = q3
            bautura_selectata = "Cappuccino-ul"
        elif inp == "H":
            stare = q4
            bautura_selectata = "Ciocolata caldă"
        else:
            print(f"Eroare: Opțiune invalidă ({inp}). Reîncearcă!\n")
            continue 

        while True:
            confirmare = input(f"Confirmi comanda pentru {bautura_selectata}? (O - Da, D - Anulează): ").strip().upper()
            if confirmare == "O":
                stare = q5
                comanda_confirmata = True
                break 
            elif confirmare == "D":
                stare = q0
                comanda_confirmata = False
                print("Comanda anulată. Alege din nou o băutură!\n")
                break
            else:
                print("Eroare: Introdu doar 'O' pentru confirmare sau 'D' pentru anulare!")

        if comanda_confirmata:
            return f"{bautura_selectata} dumneavoastră este gata!"

if __name__ == "__main__":
    print(automat_finit())
