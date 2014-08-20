line = [3,5,4,2]
line2 =[4,2,6,5]
line3=[7,3,5,4]

set = [line,line2,line3]
print(line,line2,line3,sep="\n")
g = eval(input("enetr  line num"))
g2 = eval(input("enetr  line num"))

for i in range(4):
    if set[g][0] == set[g2][i]:
        print(set[g][0],"A")
        break
for i in range(4):
    if set[g][1] == set[g2][i]:
        print(set[g][1],"B")
        break
for i in range(4):
    if set[g][2] == set[g2][i]:
        print(set[g][2],"C")
        break
for i in range(4):
    if set[g][3] == set[g2][i]:
        print(set[g][3],"D")
        break
