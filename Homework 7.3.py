 #В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
 #Данный метод позволяет организовать ячейки по рядам.
#Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
#Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
class Cell():
    def __init__(self, num_cells):
        self.num_cells=int(num_cells)

    def __str__(self):
        return f"Результат операции {self.num_cells*'*'}"

    def __add__(self, other):
        return Cell(self.num_cells+other.num_cells)

    def __sub__(self, other):
        if self.num_cells - other.num_cells>0:
            return Cell(self.num_cells - other.num_cells)
        else:
            return "данные клетки не способны к делению"

    def __mul__(self, other):
        return Cell(self.num_cells * other.num_cells)

    def __mul__(self, other):
        return Cell(self.num_cells * other.num_cells)


    def __truediv__(self, other):
        return Cell(round(self.num_cells // other.num_cells))

    def make_order(self, cell_in_row):
        row=''
        for i in range(int(self.num_cells //cell_in_row)):
            row+=f" {'*'* cell_in_row} \n"
        row+=f"{' '+ '*'* (self.num_cells % cell_in_row)}"
        return row


cell1=Cell(8)
cell2=Cell(24)
print(cell2)
print(cell1+cell2)
print(cell1-cell2)
print(cell1*cell2)
print(cell1/cell2)
print(cell1.make_order(3))