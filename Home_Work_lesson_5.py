
# number = 10234003234
# new_number = str(number)
# print(new_number.count("0"))

######################################################################################
# zero = []
# number = 1020987400330000
# new_number = list(str(number)[::-1])
# for i in new_number:
#     if i == "0":
#         zero.append(i)
#     else:
#         break
#
# print(len(zero))

###########################################################################################

# my_list_1 = [ 1,2,34,556,7,44,22]
# my_list_2 = [13,434,5,88,9987,48888]
# my_results = []
# my_results.append(my_list_1[1::2])
# my_results.append(my_list_2[0::2])
# print(my_results)

################################################################################

# my_list = [1,2,3,4]
# new_list=[]
# new_list = my_list[1:]
# new_list.append(my_list[0])
# print(new_list)

##################################################################################

# my_list = [1,2,3,4]
# my_list += (my_list)
# my_list.pop(0)
# my_list= my_list[0:4]
# print(my_list)

####################################################################################

res = []
d='Артему 7 лет он старше Влада на 2 года и младше Серсея на 1 год'.split()
for valeo in d:
    if valeo.isdigit():
        res.append(int(valeo))

print(sum(res))
