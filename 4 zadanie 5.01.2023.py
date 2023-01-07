# Mając na wejściu pewną listę liczb. Wypisz po kolei daną liczbę wraz z informacją
# czy jest parzysta czy nieparzysta.
# wejście: A = [7, 14, 41, 18, 9]
# wyjście:
# 7 - nieparzysta
# 14 - parzysta
# 41 - nieparzysta
# 18 - parzysta
# 9 - nieparzysta

list = [7, 14, 41, 18, 9]

for x in list:
    print(x)
    if x%2:
        print("- nieparzysta")
    else:
        print("- parzysta")
