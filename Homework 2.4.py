my_text=input("введите фразу из нескольких слов с пробелами")
split_text=my_text.split()
for el in split_text:
	if len(el)>10:
	  print(split_text.index(el)+1, el[:10])
	else:
		print(split_text.index(el)+1, el)