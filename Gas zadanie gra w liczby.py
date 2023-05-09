#losujesz liczbę z przedziału 1 - 20 powiedzmy.
# Użytkownik stara się zgadnąć i dostaje informację zwrotną
# czy trafił (wtedy koniec gry jakiś print z gratulacjami), czy więcej/mniej

# użyć import random
# użyć while

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






# while user_choice < random_num:
#     print(int(input("Wpisz większą liczbę: ")))
# user_choice_2 = print(int(input("Wpisz większą liczbę: ")))
#
# while user_choice > random_num:
#     print(int(input("Wpisz mniejszą liczbę: ")))
# user_choice_2 = print(int(input("Wpisz mniejszą liczbę: ")))