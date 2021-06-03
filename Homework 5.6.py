subj = []
hours=[]
with open("subjects.txt",'r+') as my_f:
    for line in my_f:
        line_1=line.split(':')
        subj.append(line_1[0])
        line_2=line.split(' ')
        res=[int(i) for i in line_2 if i.isdigit()]
        hours.append(sum(res))
        final_dict=dict(zip(subj,hours))
print(final_dict)









