#collect data
marks = input("Enter a space-separated list of marks: \n")


#categorise the data
first= []
upper_sec = []
lower_sec = []
third = []
fail = []



splited = marks.split(" ")
for i in splited:
    if 75 <= int(i):
        first.append(i)
        first.sort()
    elif 70 <= int(i) < 75:
        upper_sec.append(i)
        upper_sec.sort()
    elif 60 <= int(i) < 70:
        lower_sec.append(i)
        lower_sec.sort()
    elif 50 <= int(i) < 60:
        third.append(i)
        third.sort()
    else:
        fail.append(i)
        fail.sort()





#print the rest.

print("1 |",len(first)*"X",sep='')
print("2+|",len(upper_sec)*"X",sep='')
print("2-|",len(lower_sec)*"X",sep='')
print("3 |",len(third)*"X",sep='')
print("F |",len(fail)*"X",sep='')