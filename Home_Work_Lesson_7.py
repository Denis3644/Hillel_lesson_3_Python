# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
#
# my_list = ["qwe","rty","uio","asd","fgh"]
# my_result = []
# for index in range(len(my_list)):
#     valeo = my_list[index]
#     if index % 2:
#         new_valeo = valeo[::-1]
#     else:
#         new_valeo = valeo
#     my_result.append(new_valeo)
# print(my_result)

#######################################################

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
# new_list = []
# my_list = ["abc","dfg","uoo","aer","yua","a"]
# for simbol in my_list:
#     if simbol [0] == "a":
#         new_list.append(simbol)
# print(new_list)

######################################################################3
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
# new_list = []
# my_list = ["bac","dfg","uao","aer","yuy","a"]
# for simbol in my_list:
#     if "a" in simbol :
#         new_list.append(simbol)
# print(new_list)

#######################################################################
# 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

# my_list = ["abc","dfg","uoa",123,5567]
# new_list = [value for value in my_list if type(value) == str]
# print(new_list)
#####################################################################
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

# only_str =[]
# my_str = "hillel lesson 7 tesk 5"
# for line in set(my_str):
#     colithcestvo = my_str.count(line)
#     if colithcestvo == 1:
#         only_str.append(line)
# print(only_str)
#######################################################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
# stroka_1 = "Сегодня идет дождь"
# stroka_2 = "Завтра будет солнце"
#
# stroka_1_set = set(stroka_1)
# stroka_2_set = set(stroka_2)
#
# spisok_obchii = list(stroka_1_set.intersection(stroka_2_set))
# print(spisok_obchii)
###############################################################################
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
stroka_1 = "aassddssfeuuu"
stroka_2 = "aaasssssdfe"
stroka_1_set = set(stroka_1)
stroka_2_set = set(stroka_2)
stroka_3 = []
for index in stroka_1_set.intersection(stroka_2_set):
    if stroka_1.count(index) == 1 and stroka_2.count(index) == 1:
        stroka_3.append(index)
print(stroka_3)

#######################################################################################
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# person = {"firstname":"Tolstoy",
#           "name" : "Leo" ,
#           "age" : "36",
#           "adress" : { "country" : "Ukraine",
#                        "city": "Dnipro",
#                        "street" : "Heroiv 11"},
#           "work" : {"restrant" : "Home park",
#                     "position" : "Manadger"}}
# print(person["work"]["restrant"])

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов)
# tort = {"ingridient" : { "korzhi" : {"muka" : 200,
#                      "moloko": 250,
#                      "maslo" : 150,
#                      "yaitso": 90},
#                          "crem" : {"sahar" : 240,
#                                    "maslo" : 160,
#                                    "vanil" : 40,
#                                    "smetana" : 200},
#                          "glazur" : {"cacao" : 30,
#                                      "sahar" : 180,
#                                      "maslo" : 140}}}
# print(tort["ingridient"]["crem"]["vanil"])






