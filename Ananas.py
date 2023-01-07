#Na wejściu masz ciąg znaków, przykładowo „ananas”. Policz ile razy występuje każda literka.

#1. przygotowuję sobie pusty słownik
#2. przechodzę literka po literce przez wyraz za pomocą pętli for
#3. jeśli literki nie ma w słowniku to wrzucam do słownika literkę jako klucz i ustawiam jej wartość na 1
#4. jeśli literka już jest w słowniku to zwiększam jej wartość o 1

dict = {
}
word = "ananas"

for x in word:
    print(x)
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] +=1
print(dict)





# 1) Tworzę słownik - dict - z przykładowego wyrazu
# 2) Przerabiam przykładowy wyraz na index
# 3) Tworzę funkcję def z wyrazu która oblicza ile razy występuje każda literka

#word.count("")

#ilość każdej litery


#def word_list
    #count("ananas")



#for number_of_liter in word:

