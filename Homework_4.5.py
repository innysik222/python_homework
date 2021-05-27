from functools import reduce
lst=[el for el in range(100,1001) if el%2==0]
def mult_element(prev_el, el):
	return prev_el*el

print(reduce(mult_element, lst))