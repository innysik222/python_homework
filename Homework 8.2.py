# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#Проверьте его работу на данных, вводимых пользователем.
#При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class MyZeroDivError(Exception):
    def __str__(self):
        return "Делить на ноль нельзя"


while True:
    try:
        divident = int(input('divident: '))
        divider = int(input('divider: '))
        if divider==0:
            raise MyZeroDivError
    except MyZeroDivError as e:
        print(e)
    else:
        print(divident/divider)
