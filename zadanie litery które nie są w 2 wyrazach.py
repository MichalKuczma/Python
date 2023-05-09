# Zwróć listę takich literek, które NIE występują w drugim wyrazie.
# konstantynopol
# #tangens

# o, t, y, o, p, l

wyraz_1 = 'konstantynopol'
wyraz_2 = 'tangens'

# print(set(wyraz_1))
# print(set(wyraz_2))

nie_wystepuja = set(wyraz_1).difference(set(wyraz_2))

print(nie_wystepuja)



