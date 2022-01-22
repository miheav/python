
class TrafficLight:


    __color  = 'red'

    def running(self):
        counter = 0
        while (1):
            counter += 1
            if(self.__color == 'red' and counter >= 7):
                self.__color = 'yellow'
                counter = 0
            elif(self.__color == 'yellow' and counter >= 2):
                self.__color = 'green'
                counter = 0
            elif(self.__color == 'green' and counter >= 4):
                self.__color = 'red'
                counter = 0
                break
            print(self.__color)


tl = TrafficLight()

tl.running()