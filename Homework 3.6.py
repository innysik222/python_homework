def int_func(low_str):
    return low_str.capitalize()


my_text = input("Введите текст из латинских букв через пробел в нижнем регистре")

text_list = my_text.split(' ')
for word in text_list:
    print(int_func(word), end=' ')

