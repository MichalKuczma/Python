import random

names_string = input("Wpisz imiona wszystkich osób, oddzelając je przecinkiem.")

names = names_string.split(", ")

number_of_names = len(names)

random_choice = random.randint(0, number_of_names -1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay)
