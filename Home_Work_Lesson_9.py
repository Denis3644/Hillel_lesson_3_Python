# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

my_list = ["qwe","rty","uio","asd","fgh"]
def create_new_list(my_list):
    my_result = []
    for index in range(len(my_list)):
        valeo = my_list[index]
        if index % 2:
            new_valeo = valeo[::-1]
        else:
            new_valeo = valeo
        my_result.append(new_valeo)

    return my_result
my_result = create_new_list(my_list)
print(my_result)

##################################################################################################################
# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

my_spisok = ["abc","dfag","uoo","aer","yua","a"]
def appennd_first_simbol_a(my_spisok):
    new_list = []
    for simbol in my_spisok:
        if simbol[0] == "a":
            new_list.append(simbol)

    return new_list
new_list = appennd_first_simbol_a(my_spisok)
print(new_list)

##################################################################################################################

# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_list = ["bac", "dfg", "uao", "aer", "yuy", "a"]
def append_a_if_a_everywhere(my_list):
    new_list = []
    for simbol in my_list:
        if "a" in simbol:
            new_list.append(simbol)

    return new_list
new_list = append_a_if_a_everywhere(my_list)
print(new_list)



##################################################################################################################
# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
my_list = ["abc","dfg","uoa",123,5567]
def creat_func(my_list):
    new_list = [value for value in my_list if type(value) == str]
    return new_list

new_list=creat_func(my_list)
print(new_list)

##################################################################################################################

# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
my_str = "hillel lesson 7 tesk 5"
def one_point(my_str):
    only_str = []
    for line in set(my_str):
        colithcestvo = my_str.count(line)
        if colithcestvo == 1:
            only_str.append(line)
    return only_str
only_str = one_point(my_str)
print(only_str)


##################################################################################################################
# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
stroka_1 = "Сегодня идет дождь"
stroka_2 = "Завтра будет солнце"

def func_simbol(stroka_1,stroka_2):
    stroka_1_set = set(stroka_1)
    stroka_2_set = set(stroka_2)
    spisok_obchii = list(stroka_1_set.intersection(stroka_2_set))
    return spisok_obchii
spisok_obchii = func_simbol(stroka_1,stroka_2)
print(spisok_obchii)

##################################################################################################################
# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
stroka_1 = "aassddssfeuuu"
stroka_2 = "aaasssssdfe"
def creat_func(stroka_1,stroka_2):
    stroka_1_set = set(stroka_1)
    stroka_2_set = set(stroka_2)
    stroka_3 = []
    for index in stroka_1_set.intersection(stroka_2_set):
        if stroka_1.count(index) == 1 and stroka_2.count(index) == 1:
            stroka_3.append(index)
    return stroka_3

stroka_3 = creat_func(stroka_1,stroka_2)
print(stroka_3)

##################################################################################################################
# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
import random
import string
names = ["Smirnof","Dnistrenko","Mikelian"]
domains = ["net","ru","com"]
alfabet = string.ascii_letters

def randome_alf(alfabet):
    a = random.choice(alfabet)
    return a

def creat_list_alf(alfabet):
    simbols = [randome_alf(alfabet) for _ in range(1, random.randint(5,7))]
    return simbols
simbols = creat_list_alf(alfabet)
simbols_2 = "".join(simbols)

def creat_e_mail(names,domains,simbols_2):
    e_mail = [random.choice(names), ".", str(random.randint(100, 999)), "@",simbols_2, ".",
              random.choice(domains)]
    e_mail_2 = "".join(e_mail)
    return e_mail_2
e_mail_2 = creat_e_mail(names,domains,simbols_2)
print(e_mail_2)