import sys

q0 = "q0"
q1 = "q1"
q2 = "q2"
q3 = "q3"
final = q3

def automat_finit():
    stare = q0
    inp =  input("Introdu un șir de caractere: ")
    for litera in inp:
        if litera < 'a' or litera > 'z':
            print(f"Caracter invalid detectat: {litera}")
            return False
        
        if litera == "c":
            if stare == q0:
                stare = q1
            elif stare == q1:
                stare = q1
            elif stare == q2:
                stare = q1
        elif litera == "a":
            if stare == q1:
                stare = q2
            elif stare == q2:
                stare = q0
        elif litera == "t":
            if stare == q1:
                stare = q0
            elif stare == q2:
                stare = q3
        else:
            if stare == q1:
                stare = q0
            elif stare == q2:
                stare = q0

    return stare == final 

if __name__ == "__main__":
    print(automat_finit())

