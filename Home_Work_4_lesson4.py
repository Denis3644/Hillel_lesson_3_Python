
my_list= [1,223,14,564,245,2,345,18]
for value in my_list:
     if value > 100:
          print(value)

###################################################
my_results = []
my_list1 = [1,5,223,14,564,245,2,345,18,67877]
for i in my_list1:
    if  i > 100:
        my_results.append(i)

print(my_results)
######################################################

my_list = [66,78,76,344]
value = len(my_list)
if value < 2:
    my_list.append(0)
else:
    new_valeo = my_list[-1] + my_list[-2]
    my_list.append(new_valeo)
print(my_list)

#######################################################
rus=[]
my_str = "0123456789"
for value1 in my_str:
    for value2 in my_str:
        rus.append(int(value1+value2))
print(rus)





















































































































