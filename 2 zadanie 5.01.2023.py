# Mając na wejściu pewną listę A. Zwróć listę B,
# w której każdy element listy A większy od 5 zostanie przemnożony przez 3.
# wejście: A = [3, 6, 4, 5, 11, 300, 2, 8, 1]
# wyjście: B = [3, 18, 4, 5, 33, 900, 2, 24, 1]

listA=[3, 6, 4, 5, 11, 300, 2, 8, 1]

listB=[]

for number in listA:
    if number > 5:
        number*=3
    listB.append(number)
print(listB)








