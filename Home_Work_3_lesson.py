#Задание 1
# первая версия решения
valeo = 130
new_valeo = valeo/2
if valeo < 100:
    print(new_valeo)
else:
    print(valeo-(valeo*2))

#вторая версия решения

new_valeo = valeo/2 if valeo < 100 else (valeo-(valeo*2))
print(new_valeo)

##################################################################################################
#Задание 2
# первая версия решения
valeo = 90
new_valeo = valeo - valeo + 1
if valeo < 100:
     print(new_valeo)
else:
     print(valeo-valeo)

#вторая версия решения
new_valeo = valeo - valeo + 1 if valeo < 100 else valeo-valeo
print(new_valeo)


########################################################################################################
#Задание 3
# первая версия решения
valeo = 5
new_valeo = True
if valeo < 100:
     print(new_valeo)
else:
     print(False)

#вторая версия решения
new_valeo = True if valeo < 100 else False
print(new_valeo)

########################################################################################################
#Задание 3
# Нечетные
my_str = "my_str"
print(my_str[1::2])
########################################################################################################
#Задание 4
# Четные
my_str = "my_str"
print(my_str[2::2])


