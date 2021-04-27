# standart_dict = {'dict': 1, 'dictionary': 2, 3: "asd"}
# short = 'dict'

# person = {"name": "Михаил",
# "возраст": 19}
#
# by_type_dict = dict (name = "Михаил", возраст = 19)

# by_type_dict = dict (короткий = короткий, длинный = 'словарь')
# standart_dict ["key_1"] = "значение_1"
# print (standart_dict)

# list_keys = list ("qwerty")
# list_values ​​= list ("123456")

# list_keys = ["asd", "zxc", "qwe", "123"]
# list_values ​​= [1,2,3,4,5,6,7,8,9,]
#
# by_zip_dict = dict (zip (list_keys, list_values))
# печать (by_zip_dict)

# list_keys = ['a', 'b']
# result = {key: 100 для ключа в list_keys}
# print (результат)

ascii_table  = { chr ( numb ): numb  for  numb  in  range ( ord ( "a" ), ord ( "z" ) +  1 )}
# печать (ascii_table)
# tmp_val = 100 в ascii_table # в проверяето ТОЛЬКО КЛЮЧИ!
# печать (tmp_val)
#
# для ключа в ascii_table: # преребор только КЛЮЧИ
# print (ключ, ascii_table [ключ])

# new_dict = ascii_table.copy ()
# new_dict ["test"] = "test"
# print (new_dict)
# печать (ascii_table)

# ключ = 100
# значение = ascii_table.get (ключ)
# print (значение)

# для ключа, значения в ascii_table.items ():
# print (ключ, значение)

dict_1  = { 1 : 11 , 2 : 2 , 3 : 33 }
dict_2  = { 14 : 11 , 24 : 22 , 3 : 11 }
#
# result = list (set (dict_1.values ​​()). пересечение (set (dict_2.values ​​())))
# print (результат)

# ключи = список (ascii_table.keys ())
# печать (ключи)

# НЕ ИМЕЕТ СМЫСЛА:
# new_dict = {значение: ключ для ключа, значение в dict_2.items ()}
# print (new_dict)

# total_dict = dict_1.copy ()
# total_dict = {}
# total_dict.update (dict_1)
# total_dict.update (dict_2)
# print (total_dict, dict_1)

# total_dict = {** dict_2, ** dict_1}
# print (total_dict, dict_2)

price_list  = [{ "хлеб" : 10 }, { "вода" : 10 }, { "банан" : 2000 }, { "вода" : 12 }]
min_value_list  = []
по  цене  в  price_list :
    min_value_list . добавить ( список ( цена . значения ()) [ 0 ])
min_value  =  min ( min_value_list )
по  цене  в  price_list :
    если  список ( price . values ()) [ 0 ] ==  min_value :
        печать ( список ( цена . ключи ()) [ 0 ])

value_list  = {}
по  цене  в  price_list :
    список_значений [ список ( цена . значения ()) [ 0 ]] =  список ( цена . ключи ()) [ 0 ]
min_value  =  min ( список_значений )
print ( список_значений [ мин ( список_значений )])