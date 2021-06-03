#НеоНеобходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json
with open("enterprise.txt",'r+') as my_f:
    name_firm=[]
    profit=[]
    for line in my_f:
        line=line.split()
        name_firm.append(line[0])
        profit.append(int(line[2])-int(line[3]))
        real_profit=[el for el in profit if el>0]
        dict_firm=dict(zip(name_firm, profit))
        av_profit= {"average_profit": round(sum(real_profit)/len(real_profit),2)}
    final_list=[dict_firm, av_profit]
    print(final_list)

with open ('my_json_f', 'w') as write_f:
    json.dump(final_list, write_f)





