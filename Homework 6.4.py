#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#Для классов TownCar и WorkCar переопределите метод show_speed.
#При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police

    def go(self):
        return f"{self.name} поехал"

    def stop(self):
        return f"{self.name} остановилась"

    def turn_right(self):
        return f"{self.name} повернул направо"

    def turn_left(self):
        return f"{self.name} повернул налево"

    def show_speed(self):
        return f"текущая скорость {self.name} равна {self.speed}"

    def if_police(self):
        if self.is_police:
            return f"полицейская машина"
        else:
            return f"не числится на баллансе полиции"

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print (f"текущая скорость {self.name} равна {self.speed}")
        if self.speed>60:
            print(f"превышение скорости для {self.name}")
        else:
            print(f"скорость в пределах допустимой")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"текущая скорость {self.name} равна {self.speed}")
        if self.speed > 40:
            print(f"превышение скорости для {self.name}")
        else:
            print(f"скорость в пределах допустимой")



class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

car1=TownCar(75, "зеленый", "мерседес", False)
car2=SportCar(120, "красный", "феррари", False)
car3=WorkCar(35, "оранжевый", "камаз", False)
car4=PoliceCar(60, "синий", "форд", True)
print(f"проверка машины: {car1.name}  {car1.if_police()}")
print(f"проверка машины: {car4.name}  {car4.if_police()}")
print(car1.go())
print(car2.stop())
print(car3.turn_left())
print(car4.turn_right())
car4.show_speed()
car1.show_speed()
car3.show_speed()


