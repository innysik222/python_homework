number=7
fl_number=9.6
my_str="Первое дз"
print (number, fl_number, my_str)
user_number=int(input ("Введите целое число"))
user_fl_number=float(input("Введите число с плавающей точкой"))
user_str=input("Введите произвольный текст")
print(user_number, user_fl_number, user_str)

time_in_second=int(input("Введите время в секундах"))
hours=time_in_second//3600
minutes=(time_in_second%3600)//60
seconds=(time_in_second%360)%60
print(f"Время в формате {hours}:{minutes}:{seconds}")

n=int(input("Введите число"))
summ_n=n+(10*n+n) +(n*100+n*10+n)
print(summ_n)

num=int(input("Введите целое положительное число"))
max=0
while num!=0:
	last_digit=num%10
	if last_digit>=max:
		max=last_digit
	num=num//10
print("Максимальная цифра из введенного числа  - ", max)

income=float(input("Введите значение выручки"))
costs=float(input("Введите значение издержек"))
if income>costs:
	print("прибыль")
	profitability =(income-costs)/income
	print("рентабельность выручки", profitability)
	employee_number=int(input("Введите количество сотрудников"))
	profit_per_person=(income-costs)/employee_number
	print("прибыль фирмы на одного сотрудника", profit_per_person)
elif income==costs:
    print("Точка безубыточности")
else:
	print("убыток")


a=float(input(" введите количество  км, которые пробежал спортсмен за первый день "))
b=int(input("введите итоговый желаемый результат в км"))
count=1
while a<b:
	a=1.1*a
	count+=1
print("Количество дней, за которое спортсмен достигнет желаемого результата - ", count)

