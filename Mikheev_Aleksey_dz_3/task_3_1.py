def num_translate(num):
    dict = {"one" : "один", "two" : "два", "three" : "три", "four" : "четыре", "five" : "пять", "six" : "шесть", "seven" : "семь", "eight" : "восемь", "nine" : "девять", "ten" : "десять"}

    return dict.get(num)



print(num_translate("ten"))
