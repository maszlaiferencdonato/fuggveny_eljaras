a = float(input("Adja meg az első számot! "))
b = float(input("Adja meg a második számot! "))

def osszehasonlit(a, b):

    if a > b:
        print(f"A nagyobb szám: {a}")
    elif a < b:
        print(f"A nagyobb szám: {b}")
    else:
        print("A két szám egyenlő.")
