def concat(s1, s2):
    return s1 + s2

def repeat(s, n):
    return s * n

def invers(s):
    return s[::-1]  

def extract(s, i, j):
    return s[i:j+1]

def replace(s, sub, new_sub):
     return s.replace(sub, new_sub, 1)


def main():
    E1 = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    E2 = {"a", "b", "c", "d", "e", "f", "g", "i", "j", "k"}
    E3 = {"x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4", "x5", "y5"}

    s1 = "abc123"
    s2 = "456x1xy2x3"
    s = "x1y1x2abc"

    print("Concatenare: ", concat(s1, s2))
    
    n = 3
    print("Repetare: ",repeat(s1, n))

    print("Invers: ",invers(s1))

    i, j = 2, 5
    print("Extractie: ",extract(s1, i, j))

    sub, new_sub = "a", "X"
    print("Inlocuire: ",replace(s1, sub, new_sub))

if __name__ == "__main__":
    main()
