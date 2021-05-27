from random import randint
lst=[randint(0,100) for i in range(10)]
print(lst)
print([lst[i] for i in range(1, len(lst)) if lst[i]>lst[i-1]])
