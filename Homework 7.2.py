#Реализовать проект расчета суммарного расхода ткани на производство одежды.
#Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#К типам одежды в этом проекте относятся пальто и костюм.
#У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
#Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани.
#Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property
from abc import ABC, abstractmethod
class Clothes(ABC):
    name=None
    @abstractmethod
    def __init__(self, v, h):
        self.h=h
        self.v=v

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_consumption(self):
        pass




class Jacket(Clothes):
    name='Jacket'

    def __init__(self, v):
        self.v=v

    def __str__(self):
        return f"production of {self.name} size {self.v}"

    @property
    def get_consumption(self):
        return self.v/6.5+0.5


class Costume(Clothes):
    name = 'Costume'

    def __init__(self, h):
        self.h = h

    def __str__(self):
        return f"production of {self.name} size {self.h}"

    @property
    def get_consumption(self):
        return 2*self.h + 0.3


jacket=Jacket(15)
costume=Costume(20)
print(jacket)
print(jacket.get_consumption)
print(costume)
print(costume.get_consumption)
print(f"total fabrique consumption - {round (jacket.get_consumption+costume.get_consumption,2)}")


