# Question 1 - Assignment 9
# Oliver Harrison
# 12 May 2014

filename = input("Enter the marks filename:\n")
f = open(filename, "r")
lines = f.readlines()
f.close()

# Find total
total = 0

for i in lines:
    comma_point = -1
    for j in i:
        comma_point += 1
        if j == ",":
            name_length = comma_point
        else:
            continue
    total += eval(i[name_length+1:])
    #total += eval(i[len(i)-3:])
    
# Find and print average 

avg = total/len(lines)
print("The average is:", "%0.2f"%round(avg, 2))

# Find and print SD
newtotal = 0
count = 0
for i in lines:
    count += 1
    comma_point = -1
    for j in i:
        comma_point += 1
        if j == ",":
            name_length = comma_point
        else:
            continue
    newtotal += (eval(i[name_length+1:]) - avg)**2


sd = (newtotal/count)**0.5
print("The std deviation is:", "%0.2f"%round(sd, 2))




# Determine students

#print("List of students who need to see an advisor:")

check_dp = 1


for i in lines:
    comma_point = -1
    for j in i:
        comma_point += 1
        if j == ",":
            name_length = comma_point
        else:
            continue
    if eval(i[name_length+1:]) < (avg - sd):
        if check_dp == 1:
            print("List of students who need to see an advisor:")
            check_dp = 2
            print(i[:name_length])
        else:
            print(i[:name_length])
        continue
            

"""for i in lines:
    if eval(i[len(i)-3:]) < (avg - sd):
        if check_dp == 1:
            print("List of students who need to see an advisor:")
            print(i[:len(i)-4])
            check_dp = 2
        else:
            print(i[:len(i)-4])"""


    

