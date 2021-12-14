for percent in range(1, 101):
    ending = ""
    b = percent % 100
    n= percent % 10
    if(percent >= 5 and percent <= 20):
        ending = "ов"
    elif(n == 1 and percent != 11):
        ending = ""
    elif(n >= 2 and n <= 4):
        ending = "а"
    else:
        ending = "ов"

    print(str(percent) + " процент" + ending)
