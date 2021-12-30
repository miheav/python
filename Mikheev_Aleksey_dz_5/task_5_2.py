#*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

n= 15
odd_to_15 = (num for num in range(1, n + 1, 2))

print(next(odd_to_15))
print(next(odd_to_15))