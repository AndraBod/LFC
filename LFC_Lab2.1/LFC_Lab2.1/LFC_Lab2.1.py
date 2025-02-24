import sys

q0 = "q0"
q1 = "q1"
q2 = "q2"
q3 = "q3"
final = q3

def automat_finit():
    stare = q0
    print("Introdu 0 si 1. Pentru a opri masina de stare apasa orice alta tasta!")
    for line in sys.stdin:
        try:
            inp = int(line.strip())
            if inp == 0:
                if stare == q0:
                    stare = q1
                elif stare == q1:
                    stare = q3
                elif stare == q2:
                    stare = q1
            elif inp == 1:
                if stare == q0:
                    stare = q2
                elif stare == q1:
                    stare = q0
                elif stare == q2:
                    stare = q3
            else:
                break 
        except ValueError:
            break  
    
    return stare == final

if __name__ == "__main__":
        print(automat_finit())
