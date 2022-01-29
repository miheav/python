import random

class LotoCard:


    def __init__(self, name):
        self.name = name
        self.numbers = []
        self.loto_card = [[" " for n in range(1,10)], [" " for n in range(1,10)], [" " for n in range(1,10)]]
        self.generate_card()

    def generate_card(self):

        for i in range(1, 16):
            new_int = random.randint(1, 90)
            self.numbers.append(self.generate_numbers(new_int))

        self.generate_rows()

    def generate_rows(self):

        b=0
        for i in range(0,15):
            if(i != 0 and i % 5 == 0):
                b = b + 1
            position = self.generate_position(random.randint(0, 8), self.loto_card[b])
            self.loto_card[b][position] = self.numbers[i]

    def generate_position(self, pos, row):
        if(row[pos] != ' '):
            pos = random.randint(0, 8)
            pos = self.generate_position(pos, row)

        return pos

    def generate_numbers(self, new_int):
        new_int = random.randint(1, 90)
        if(new_int in self.numbers):
            return self.generate_numbers(random.randint(1, 90))
        

        return new_int

    def __str__(self):
        return f'\n'+self.name+'\n'+'\n'.join([' '.join(map(str, line)) for line in self.loto_card])



class LotoGame:

    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2
        self.barrels = []

        self.winner = ''
        self.status = ''
        self.step = ''
    
    def start(self):
        self.status = 'start'
        print("Новая игра")
        print("Играют", self.player1.name, "и", self.player2.name)
        for i in range (1, 91):

            if(self.status == 'finish'):
                break
            self.step = i
            print("Ход:", i)
            self.barrels.append(self.generate_barrel())
            print("Новый бочонок:", self.barrels[-1])
            print(self.player1)

            print(self.player2)
            self.interaction()
            self.final()

        print("Игра окончена, победитель:", self.winner)


    def generate_barrel(self):
        barrel = random.randint(1, 90)

        if(barrel in self.barrels):
            barrel = self.generate_barrel()

        return barrel

    def interaction(self):
        self.player()
        self.computer()


    def player(self):

        answer = ''
        while(answer not in ['y', 'n']):
            answer = input("Зачеркнуть число? (y/n)")

        # number_in_list = self.number_in_list(self.player1)
        # if(number_in_list):
        #     answer = 'y'
        # else:
        #     answer = 'n'

        print('Ответ', answer)

        if answer == 'n' and number_in_list:
            self.status = 'finish'
            self.winner = self.player2.name

        elif answer == 'y' and not number_in_list:
            self.status = 'finish'
            self.winner = self.player2.name

        elif answer == 'y' and number_in_list:
            self.player1 = self.strike(self.player1)

    def computer(self):

        self.player2 = self.strike(self.player2)

    def strike(self, obj):

        for i in range(0,3):
            for number in range (0, 9):
                if(obj.loto_card[i][number] == self.barrels[-1]):
                    obj.loto_card[i][number] = '-'


        return obj

    def final(self):
        plauer_fin = True
        computer_fin = True 
        for i in range(0,3):
            for number in range (0, 9):
                if type(self.player1.loto_card[i][number]) == int:
                    plauer_fin = False 

                if type(self.player2.loto_card[i][number]) == int:
                    computer_fin = False 


        if(computer_fin) :
            self.status = 'finish'
            self.winner = self.player2.name
        elif(plauer_fin):
            self.status = 'finish'
            self.winner = self.player1.name

                


    
    def number_in_list(self, obj):
        if(self.barrels[-1] in obj.numbers):
            return True
        else:
            return False
        

        






human = LotoCard("Игрок")
print(human)
computer = LotoCard("Компьютер")

print(computer)


game = LotoGame(human, computer)

game.start()