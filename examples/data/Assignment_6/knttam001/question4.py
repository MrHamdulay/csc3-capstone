"""Program to output histogram representation of marks according to mark categories at UCT
Tamsin Kantor
22 April 2014"""

# get marks as a long string called mark_string
mark_string = input("Enter a space-separated list of marks:\n")

# covert mark_string to a list
mark_list = mark_string.split(" ")

# count number of fails, 3rds, lower 2nds, upper 2nds and 1sts

global fail # make global variables so that they can be used inside and outside of the for loop
fail = 0
global third
third = 0
global lowsecond
lowsecond = 0
global upsecond
upsecond = 0
global first
first = 0

for i in mark_list:
    i = int(i)
    if i < 50:
        fail += 1
    elif i < 60:
        third += 1
    elif i < 70:
        lowsecond +=1
    elif i < 75:
        upsecond += 1
    else:
        first += 1
        
# print histogram
    
print("1 |", "X"*first, sep="")
print("2+|", "X"*upsecond, sep = "")
print("2-|", "X"*lowsecond, sep = "")
print("3 |", "X"*third, sep = "")
print("F |", "X"*fail, sep = "")