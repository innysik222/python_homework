month=int(input("Введите номер месяца"))
#реализация через список
season=["зима", "весна", "лето", "осень"]
month_number=[12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if month in month_number[3:6]:
	print("весна")
elif month in month_number[6:9]:
	print("лето")
elif month in month_number[9:12]:
	print("осень")
elif month in month_number [0:3]:
    print("зима")
else:
    print ('введнный номер месяца не соответсвует ни одному из сезонов')
#реализация через словарь
month_dict ={1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
if month in month_dict.keys():
    print (month_dict[month])
else:
    print('введенный номер месяца не соответствует ни одному из сезонов')
