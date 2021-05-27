divident = int(input("введите делимое"))
divider = int(input("введите делитель"))


def division(divident, divider):

    if divider!=0:
        return divident/divider
    else:
        print("делить на ноль нельзя")
print(division(divident, divider))
print(division(12,0))
