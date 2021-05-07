

# 1) Дан список словарей persons
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# students = [{"name": "John", "age": 23}, {"name": "Jack", "age": 35},{"name": "Sasha", "age": 65}]
# min_age_list = []
# for names in students:
#     min_age_list.append(list(names.values())[1])
# min_age = min(min_age_list)
# for names in students:
#     if list(names.values())[1] == min_age:
#         print(list(names.values())[0])
##############################################################################################################
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# students = [{"name": "John", "age": 23}, {"name": "Jack", "age": 35},{"name": "Sasha", "age": 65}]
# name_list = []
# for names in students:
#     name_list.append(len(list(names.values())[0]))
#     max_name = max(name_list)
# for imya in students:
#      if len(list(imya.values())[0]) == max_name:
#          print(list(imya.values())[0])
###############################################################################################################
# в) Посчитать среднее количество лет всех людей из списка.
# students = [{"name": "John", "age": 23}, {"name": "Jack", "age": 35},{"name": "Sasha", "age": 65}]
# name_years_list = []
# for years in students:
#     name_years_list.append(list(years.values())[1])
# summa_year = sum(name_years_list)
# colvo = len(name_years_list)
# srednee_2 = summa_year/colvo
# print(srednee_2)
########################################################################################################
# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# dict_1 = {"Games" : "Xbox","Nintendo" : 360, "VR" : "AR" }
# dict_2 = {"Games" : "Psp", "Sega" : 180, "VR" : "MR"}
# result = list(set(dict_1.keys()).intersection(set(dict_2.keys())))
# print(result)
########################################################################################################
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# dict_1 = {"Games" : "Xbox","Nintendo" : 360, "VR" : "AR", "abc" : 33 }
# dict_2 = {"Games" : "Psp", "Sega" : 180, "VR" : "MR"}
# result = list(set(dict_1.keys()).difference(set(dict_2.keys())))
# print(result)
########################################################################################################
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# dict_1 = {"Games" : "Psp","Nintendo" : 360, "VR" : "AR", "DD": "CC"}
# dict_2 = {"Games" : "Psp", "Sega" : 180, "VR" : "AR", "NN":" DDRR"}
# result = list(set(dict_1.keys()).difference(set(dict_2.keys())))
# dict_new = {key: value for key, value in dict_1.items() if key in result}
# print(dict_new)


