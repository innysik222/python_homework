my_f=open("salary.txt","r")
salary2=my_f.read()
#print(salary2)
salary3=salary2.split('\n')
#print(salary3)
low_pay_employee=[]
wage=[]
for el in salary3:
    el=el.split()
    if int(el[1])<20000:
        low_pay_employee.append(el[0])
    wage.append(el[1])
print(f"сотрудники {low_pay_employee} имеют оклад менее 20000, средний оклад сотрудников -{sum(map(int, wage))/len(wage)}")


