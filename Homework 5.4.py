#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
with open("numbers.txt","r") as my_f:
    rus_numbers=["Один", "Два", "Три", "Четыре"]
    new_list=[]
    i = 0
    for line in my_f:
        line=line.split(" ")
        line.pop(0)
        line.insert(0,rus_numbers[i])
        i+=1
        new_line=(' ').join(line)
        new_list.append(new_line)
        print(new_line)
with open("new_numbers.txt",'w') as new_f:
    new_f.writelines(new_list)






