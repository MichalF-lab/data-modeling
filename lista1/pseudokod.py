import random
wynik =[]
tab = [1, 2, 3, 4, 5]
while True:
    tab_copy = tab[:]
    random.shuffle(tab_copy)
    if tab_copy not in wynik:
        wynik.append(tab_copy)
    if len(wynik) == 120:
        break

print(wynik)
