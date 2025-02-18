def concatenare (s1,s2):
    return s1+s2

def invers (s):
    return s[::-1]

def substitutie (s, a, b):
   rez = ""
   for i in s:
      if i == a:
        rez = rez + b
      else:
        rez = rez+i
   return rez

def lungime (s):
    return len(s)

def main():

   A = {'a', 'b', 'c'}
   B = {'x', 'y', 'z'}
   C = {'1', '2', '3'}

   s1="abc"
   s2="xyz"
   s3="123"

   print (concatenare(s1,s2))
   print (invers (s1))
   print (substitutie (s1, "a", "b"))
   print (lungime (s1))



if __name__ == "__main__":
    main()
