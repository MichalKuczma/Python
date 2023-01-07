# Mając na wejściu pewną listę A. Zwróć listę B, w której co drugi element listy A
# będzie pomnożony przez 2.
# wejście: A = [2, 6, 34, 15, 11, 87, 2, 4]
# wyjście: B = [2, 12, 34, 30, 11, 174, 2, 8]

# Plan działania:
# 1. Indeksuje liczby z listy A
# 2. Piszę funkcję która mnoży co 2 liczbę z indexu / liczbę o indexie paarzystym *2

listA = [2, 6, 34, 15, 11, 87, 2, 4]
listB = []
# n = number
#for n in listA:
    #print(n)
#wybieram co drugi element z listy czyli 6;15;87;4 >> czyli index nieparzysty
#elements_to_mp = listA[1::2]
#print(elements_to_mp)
for index, n in enumerate(listA):
    if index % 2 != 0:
        n*=2
        listB.append(n)
    else:
        listB.append(n)
print(listB)

