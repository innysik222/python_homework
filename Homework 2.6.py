
num=int(input("Введите количество товаров в каталоге"))
dict_item=[]
lst=[]
anatitics={}
for i in range (1,num+1):
    dict_item=dict({"название": input('введите название'), "количество": input('введите количество'), "цена": input('введите цену'), "ед.": input('введите единицу измерения')})
    lst.append((i,dict_item))
    analitics=({'название': dict_item.get('название'), 'цена': dict_item.get('цена'), 'количество': dict_item.get('количество'), 'ед.': dict_item.get('ед.')})


print(lst)
print(analitics)


#{“название”: [“компьютер”, “принтер”, “сканер”],“цена”: [20000, 6000, 2000],“количество”: [5, 2, 7],“ед”: [“шт.”]}
#name_list=[dict_1.get('название'), dict_2.get('название'), dict_3.get('название')]
#price_list=[dict_1.get('цена'), dict_2.get('цена'), dict_3.get('цена')]
#ammount_list=[dict_1.get('количество'), dict_2.get('количество'), dict_3.get('количество')]
#commodity_list=list(set([dict_1.get('ед.'), dict_2.get('ед.'), dict_3.get('ед.')]))
#final_dict={'название': name_list, 'цена': price_list,'количество': ammount_list, 'ед.': commodity_list}
#print(final_dict)