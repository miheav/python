dict = {"one" : "один", "two" : "два", "three" : "три", "four" : "четыре", "five" : "пять", "six" : "шесть", "seven" : "семь", "eight" : "восемь", "nine" : "девять", "ten" : "десять"}

def num_translate(num):

    return dict.get(num)



print(num_translate("ten"))
