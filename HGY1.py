import random

def random_gyumik(db):
   
    gyumolcsok = ["alma", "körte", "szilva", "barack", "málna", "füge", "eper"]
    return [random.choice(gyumolcsok) for _ in range(db)]

print(random_gyumik(19))  
print(random_gyumik(24))  