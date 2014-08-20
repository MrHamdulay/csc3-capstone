# Emmalene Naicker
# NCKEMM001
# Question 4

x = ["1 ", "2+", "2-", "3 ", "F "]
count = ['', '', '', '', '']

# Ask user to enter the marks and convert to array
mrks = input("Enter a space-separated list of marks:\n").split() 

for i in range(len(mrks)): 
    mrks[i] = eval(mrks[i])

#check which category each mark falls in and add X to that respective category

for mrk in mrks: 
    if mrk >= 75:
        count[0] += "X"
    elif mrk >= 70:
        count[1] += "X"
    elif mrk >= 60:
        count[2] += "X"
    elif mrk >= 50:
        count[3] += "X"
    else:
        count[4] += "X"
        
for i in range(len(x)):
    print(x[i], "|", count[i], sep = "") 
        
