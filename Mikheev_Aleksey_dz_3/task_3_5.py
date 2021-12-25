# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

#             Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]


# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num, flag = False):
    jokes = []
    if(flag == False):
        for i in range(num):
            noun = random.choice(nouns)
            adverb = random.choice(adverbs)
            adjective = random.choice(adjectives)

            jokes.append(f'{noun} {adverb} {adjective}')
    
    else:
        if num > min(len(nouns), len(adverbs), len(adjectives)):
            return 'No way'
        forbidden = []
        for i in range(num):
            noun = ''
            adverb = ''
            adjective = ''
            while (noun == '' and adverb == '' and adjective == ''):
                noun = random.choice(nouns)
                adverb = random.choice(adverbs)
                adjective = random.choice(adjectives)
                if(noun in forbidden or adverb in forbidden or adjective in forbidden):
                    noun = ''
                    adverb = ''
                    adjective = ''
                    continue

                forbidden.append(noun)
                forbidden.append(adverb)
                forbidden.append(adjective)
                jokes.append(f'{noun} {adverb} {adjective}')

            

    return jokes

to_print = get_jokes(52, True)
print(to_print)