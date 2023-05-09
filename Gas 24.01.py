#Było już zgadywanie (komputer losuje liczbę i Ty zgadujesz,
# on Ci mówi czy większa czy mniejsza). Teraz odwrócimy strony.
# To Ty wybierzesz liczbę od 1- 20, a komputer niech zgaduje (czyli tak naprawdę niech losuje).
# Możesz mu sam mówić czy większa czy mniejsza, a możesz to zrobić już automatycznie,
# ale niech ta informacja zawsze będzie wypisana na ekranie.
# i w zależności od tej informacji niech losuje już w odpowiednio zmienionym zakresie.
# Jak odgadnie to wypisz ile prób mu to zajęło

import random

user_choice = int(input("Wpisz liczbę od 1 do 20: "))
still_guessting = True

count_of_tries = 0


while still_guessting:
    computer_random_choice_first = random.randint(1, 20)
    print(computer_random_choice_first)
    count_of_tries += 1
    if computer_random_choice_first == user_choice:
        still_guessting = False
        print("Gratulacje wygrałeś!")
    elif user_choice > int(computer_random_choice_first):
        print("Wybierz mniejszą liczbę: ")
    else:
        print("Wybierz większą liczbę: ")

        left_end = 1 + computer_random_choice_first
        right_end = 20 - computer_random_choice_first
        computer_random_choice_second = random.randint(left_end, right_end)

        print(computer_random_choice_second)

print(count_of_tries)
