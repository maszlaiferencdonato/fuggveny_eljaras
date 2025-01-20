import math

def kerulet(*args):

    if len(args) == 1:
        return 4 * args[0]
    
    elif len(args) == 2:
        return 2 * (args[0] + args[1])
    
    elif len(args) == 3:
        a, b, c = args
        if a + b > c and a + c > b and b + c > a:
            return a + b + c
        
    else:
        return sum(args)

print("Négyzet kerülete:", kerulet(3))
print("Téglalap kerülete:", kerulet(4, 5))
print("Háromszög kerülete:", kerulet(6, 7, 8))
print("Sokszög kerülete:", kerulet(9, 10, 11, 12))