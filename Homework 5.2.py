my_f=open("test.txt","r")
text_lines=my_f.readlines()
#print(text_lines)

print (f"Количество строк в файле - {len(text_lines)}")
my_f.close()
with open("test.txt","r") as my_f:
    text_lines=my_f.read()
    split_lines=text_lines.split('\n')
    #print(split_lines)
    count=0
    for elem in split_lines:
        elem=elem.split()
        count+=1
        print(f"Количество слов в строке {count} -  {len(elem)}")


