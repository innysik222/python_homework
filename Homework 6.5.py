#Реализовать класс Stationery (канцелярская принадлежность).
#Определить в нем атрибут title (название) и метод draw (отрисовка).
#Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#В каждом из классов реализовать переопределение метода draw.
#Для каждого из классов методы должен выводить уникальное сообщение.
#Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title=title
    def draw(self):
        return "запуск отрисовки"

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"выбран {self.title}: отрисовка ручкой"

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"выбран {self.title}: отрисовка карандашом"

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"выбран {self.title}: отрисовка маркером"

pencil=Pencil("карандаш")
pen=Pen("ручка")
handle=Handle("маркер")
st=Stationery("канцелярия")
print(st.draw())
print(pencil.draw())
print(pen.draw())
print(handle.draw())
