
def is_palindrom(s):
    return s == s[::-1]

def generare_palindroame(E, max_len):
    def generate_combinations(E, length, prefix=""):
        if length == 0:
            if is_palindrom(prefix):
                print(prefix)
            return
        for char in E:
            generate_combinations(E, length - 1, prefix + char)
    
    for length in range(1, max_len + 1):
        print(f"Palindroame de lungime {length}:")
        generate_combinations(E, length)
        print()

def main():

    E = ["0", "1", "2"] 
    max_len = 5
    generare_palindroame(E, max_len)

if __name__ == "__main__":
    main()
