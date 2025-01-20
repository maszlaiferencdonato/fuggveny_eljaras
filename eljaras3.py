def osszehasonlitas(szam1, szam2):

    if szam1 > szam2:
        print(f"A {szam1} a nagyobb szám.")
    elif szam1 < szam2:
        print(f"A {szam2} a nagyobb szám.")
    else:
        print(f"A két szám egyenlő: {szam1} = {szam2}.")


osszehasonlitas(3, 10)
osszehasonlitas(7, 5)
osszehasonlitas(5, 5)
