str = input("введите список цифр через пробел ")
count = 0
while "q" not in str:
    sum_int=sum(list(map(int,str.split(' '))))
    count+=sum_int
    print(count)
    str=input()
else:
    str_split=str.split(' ')
    str_split.remove('q')
    sum_lst=sum(list(map(int, str_split)))
    print(count+sum_lst)
print("выход: введен секретный символ")



