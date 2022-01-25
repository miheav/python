class Car:

    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name 

    def go(self):
        print("Поехала")

    def stop(self):
        print("Остановка")

    def turn(self, direction):
        print(f'Поворот {direction}')

    def show_speed(self):
        print(f"Скорость: {self.speed}")



class TownCar(Car):

    def show_speed(self):
        super().show_speed()

        if(self.speed > 60):
            print("Превышение скорости")


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()

        if(self.speed > 60):
            print("Превышение скорости")


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True



sport_car = SportCar(240, 'Красная', 'Спортивная машина')
town_car = TownCar(140, 'Серая', 'Городская машина')
work_car = WorkCar(90, 'Желтая', 'Рабочая машина')
police_car = PoliceCar(210, 'Синяя', 'Полицейская машина')

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('left')