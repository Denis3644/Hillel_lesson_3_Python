import random
nam_sluchainoe = random.randint(1,100)
print("Привет, давай сыграем")
print("Угадай число которое я загадал за меньшее колличество попыток ")
k=0
while True:
    namber = int(input())
    if nam_sluchainoe == namber:
        print("Поздравляем!!! Вы угадали")
        break
    elif nam_sluchainoe > namber:
        print("Загаданное число больше ")
    elif nam_sluchainoe < namber:
        print("Загаданное число меньше ")
    k = k + 1
    print("Колличество твоих попыток =", k)






