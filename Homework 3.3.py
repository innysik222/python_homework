def my_func(x,y,z):
	ls=[]
	ls.append(x)
	ls.append(y)
	ls.append(z)
	ls.remove(min(ls))
	sum_max=sum(ls)
	return sum_max
print(my_func(5,9,56))