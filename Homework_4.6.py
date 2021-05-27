from itertools import count, cycle
for el in count(3):
	if el>10:
		break
	print(el)
count=0
for el in cycle("python"):
	if count >11:
		break
	print(el)
	count+=1