
duration = [22, 60, 150, 4122, 40015, 150000]

for data in duration:
    print("duration = " + str(data))
    if (data < 60):
        print (str(data) + " сек")
    elif (data < 60*60):
        minutes = data // 60
        seconds = data % 60
        print (str(minutes)+" мин " + str(seconds) + " сек")
    elif (data < 60*60*24):
        minutes = data // 60
        seconds = data % 60
        hours = minutes // 60
        minutes = minutes % 60
        print (str(hours) + " ч " + str(minutes)+" мин " + str(seconds) + " сек")
    else:
        minutes = data // 60
        seconds = data % 60
        hours = minutes // 60
        minutes = minutes % 60
        days = hours // 24
        hours = hours % 24
        print (str(days) + " д " + str(hours) + " ч " + str(minutes)+" мин " + str(seconds) + " сек")
    # print(str(data) + " секунд соответствуют: ")

    # # Секунды
    # print("Секунды: " + str(data))

    # # a Минуты
    # minutes = data // 60
    # seconds = data % 60

    # print("Минуты: " + str(minutes) + " Секунды: " + str(seconds))

    # # b Часы
    # hours = minutes // 60
    # minutes = minutes % 60

    # print("Часы: " + str(hours) + " Минуты: " +
    #       str(minutes) + " Секунды: " + str(seconds))

    # # Дни
