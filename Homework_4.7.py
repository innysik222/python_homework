def fact(n):
    res = 1
    for el in range(1, n + 1):
        res *= el
    yield res


print(fact(4))

for el in fact(4):
    print(el)
#генератор факториала через модуль math
from math import factorial
def fact_2(n):
   yield factorial(n)

print(fact_2(4))
for el in fact_2(4):
    print(el)
