# Mając na wejściu pewną listę wyrazów A. Zwróć listę B, w której
# każdy wyraz z listy A zostanie ucięty do ilości znaków odpowiadającej jego pozycji w liście/indeksowi.
# wejście: A = ["kurtka", "hokej", "jabłko", "granat", "ananas", "katafalk"]
# wyjście: B = ["", "h", "ja", "gra", "anan", "kataf"]

list_A = ["kurtka", "hokej", "jabłko", "granat", "ananas", "katafalk"]
list_B = []

# word = w
# letter = l

for index, element in enumerate(list_A):
    list_B.append(element[:index])
    print(list_B)
