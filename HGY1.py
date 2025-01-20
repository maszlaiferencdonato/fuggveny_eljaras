import random

def random_gyumik():
   
    gyumolcsok = ["alma", "körte", "szilva", "barack", "málna", "füge", "eper"]
    return [random.choice(gyumolcsok) for i in range(30)]

print(random_gyumik())