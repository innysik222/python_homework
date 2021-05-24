my_list=[7,5,3,3,2]
number=int(input("введите число, отличное от 0"))
len_list=len(my_list)
while number!=0:
    for i in range (len_list):
        if my_list[0]<number:
            my_list.insert(0, number)
        elif my_list[-1]>number:
            my_list.insert(len(my_list), number)
        elif my_list[i]==number:
            my_list.insert(i+1, number)
            break
        elif my_list[i]>number and my_list[i+1]<number:
            my_list.insert(i+1, number)
            break
    len_list+= 1
    print(my_list)

    number=int(input("введите число, отличное от 0"))

else:
    print ("выход")


