#2. Napisz program, który przyjmując na wejściu dwa wyrazy, zwróci literki,
# które występują w obu. Np. „konstantynopol” i „tangens”
# Literki: a, n, s, t

str1 = input("Wpisz pierwszy wyraz: ")
str2 = input("Wpisz drugi wyraz: ")

common_letters = []

for letter in set(str1):
    print(letter)
    if letter in str2:
        common_letters.append(letter)
print(set(common_letters))
print(sorted(set(common_letters)))
