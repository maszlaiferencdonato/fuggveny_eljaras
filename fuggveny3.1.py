def harommal_oszthatok(szamok):
    return sum(1 for szam in szamok if szam % 3 == 0)

szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Hárommal osztható számok száma:", harommal_oszthatok(szamok))