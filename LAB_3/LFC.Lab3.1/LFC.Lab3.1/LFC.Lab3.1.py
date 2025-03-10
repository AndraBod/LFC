def automat_finit():
    q0 = "q0" 
    q1 = "q1"
    q2 = "q2"
    q3 = "q3" 
    q4 = "q4"
    stare = q0
    bautura_selectata = None

    while True:
        print("\n    Meniu Băuturi    ")
        print("C - Cafea")
        print("T - Ceai")
        print("A - Cappuccino")
        print("H - Ciocolată caldă")
        print("OK - Confirmare comandă\n")

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
        elif inp == "OK":
            print("Trebuie să comanzi o băutură.") 
            continue 
        else:
            print(f"Eroare: Opțiune invalidă ({inp}). Reîncearcă!\n")
            continue

        if stare in [q1, q2, q3, q4]:
            confirmare = input("Doriți să confirmați cu 'OK'? ").strip().upper()
            if confirmare == "OK":
                print(f"{bautura_selectata} dumneavoastră este gata!")
                stare = q0  
                bautura_selectata = None  
            else:
                print("Comanda a fost anulată. Reveniți la meniul principal.")
                stare = q0  
                bautura_selectata = None 


if __name__ == "__main__":
    automat_finit()
