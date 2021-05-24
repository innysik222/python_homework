lst=[]
number=int(input('введите число элемнтов списка'))
count_num=0
el=0
while count_num<number:
    lst.append(input(f'введите {count_num+1} элемент списка'))
    count_num+=1
for i in range (len(lst)//2):
    lst[el],lst[el+1]=lst[el+1],lst[el]
    el+=2
print(lst)

