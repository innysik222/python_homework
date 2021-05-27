from sys import argv
script_name, work_in_hour, rate_per_hour, bonus=argv
print("Рассчет зп", script_name)
print("Выработка в часах", float(work_in_hour))
print("Ставка в час", float(rate_per_hour))
print("Бонус", float(bonus))
wage=float(work_in_hour)*float(rate_per_hour)+float(bonus)
print("зар. плата", wage)

