''' program that makes a histogram representation of marks
nic findlay
22 april 2014'''


marks = input("Enter a space-separated list of marks:\n").split()
marks.sort()
marks.reverse()
counter = []
sectors = ['1 ', '2+', '2-', '3 ', 'F ']
catagory = []
for i in marks:
            if eval(i) >= 75:
                        catagory.append('1 ')
            elif eval(i) >= 70:
                        catagory.append('2+')
            elif eval(i) >= 60:
                        catagory.append('2-')
            elif eval(i) >= 50:     
                        catagory.append('3 ')
            elif eval(i) >= 0:
                        catagory.append('F ')

no_dup = list(set(catagory))   #removes duplicates
no_dup.sort()
index = 0
mark_count = []
for i in sectors:
            if i in catagory:
                        mark_count.append(catagory.count(i))
                        index += 1
            else: 
                        mark_count.append(0)
                        index += 1
                       


for i in range(len(sectors)):
            print(sectors[i] + '|' + mark_count[i] * 'X')