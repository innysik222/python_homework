#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open("count.txt", "w+") as count_number:
    count_number.write(input("введите цифры через пробел"))

with open("count.txt", 'r') as count_number:
    content=count_number.read()
    sum_content=sum(map(int,content.split()))
    print(f'Сумма чисел файла  - {sum_content}')