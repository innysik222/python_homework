class Warehouse:
    def __init__(self, name):
        self.name=name
        self.items=[]




    def __str__(self):
        res='\n'.join(str(item) for item in self.items)
        return f'на складе {self.name} хранятся позициии: \n {res}'


    def accept_equipment(self, equipment):
        self.items.append(equipment)

    def ship_equipment(self, equipment):
            if not equipment in self.items:
                raise ValueError
            self.items.remove(equipment)







    def move_equipment(self, equipment, another_warehouse):
        self.ship_equipment(equipment)
        another_warehouse.accept_equipment(equipment)





class Equipmet:
    def __init__(self, model, price, weight):
        if not ((type(price) is int or type(price) is float) and price>0):
            raise ValueError ('цена должна быть положительным числом')
        if not ((type(weight) is int or type(weight) is float) and weight>0):
            raise ValueError ('вес должен быть положительным числом')

        self.model=model
        self.price=price
        self.weight=weight

    def __str__(self):
        return f'{self.itemname} {self.model} цена {self.price} вес {self.weight}'

class Printer(Equipmet):
    itemname='Принтер'
    def __init__(self, model, price, weight, color):
        super().__init__(model, price, weight)
        self.color=color



class Scaner(Equipmet):
    itemname='Сканер'
    def __init__(self, model, price, weight, capacity):
        super().__init__(model, price, weight)
        self.capacity=capacity

class Xerox(Equipmet):
    itemname="Ксерокс"
    def __init__(self, model, price, weight, speed):
        super().__init__(model, price, weight)
        self.speed=speed

p=Printer('lt54', 7, 10, 'цветной')
s=Scaner('gf456', 6700, 5, 'мульти')
x=Xerox('fge67', 5600, 6, '60 стр/мин')
print(s)
warhouse_msk=Warehouse('Moscow')
warhouse_spb=Warehouse('Spb')
warhouse_kr=Warehouse('Krasnoyarsk')
warhouse_msk.accept_equipment(p)
warhouse_msk.accept_equipment(s)
warhouse_msk.accept_equipment(x)
print(warhouse_msk)
warhouse_msk.move_equipment(p, warhouse_spb)
print(warhouse_spb)
warhouse_msk.ship_equipment(x)
print(warhouse_msk)
warhouse_msk.move_equipment(p, warhouse_kr)
print(warhouse_kr)



#Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
#Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.