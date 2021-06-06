#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__())
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, my_array):
        self.my_array= my_array


    def __str__(self):
        return '\n'.join(str(el) for el in self.my_array)



    def __add__(self,other):
        return Matrix([[j[0]+j[1] for j in zip(i[0],i[1])] for i in zip(self.my_array, other.my_array)])



my_matrix1=Matrix([[3,4,5], [4,5,6],[5,4,3,2,5,6]])
my_matrix2=Matrix([[2,3,6], [17,6,47], [5,6,7]])
print(my_matrix1)
print(my_matrix2)
print(my_matrix1+my_matrix2)