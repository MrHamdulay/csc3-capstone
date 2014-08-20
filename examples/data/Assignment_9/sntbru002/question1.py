"""The program thatcounts the number of learners to see advisors
By Bruce Sontshoto
17 May 2014"""

import math
a = input("Enter the marks filename:\n")

f = open(a,"r")
b = f.readlines()

f.close()
c = []
d=''
dic={}
nums=[]
#c = extract(dict)
for i in b:
    c.append(i)
    for j in c:
        if j == c[len(c)-1]:
            d = j
        else:
            d = j[:-1]
            

    #spliting whats in the list d
    x,y = d.split(",")
    dic[x]=int(y)
    nums.append(int(y))  #changing the str into an int and adding to a new list of marks which is nums
    mean = sum(nums)/len(nums)

# sum =sum(nums)
# mean
# std
# check(dict)
upp = 0.0
for value in nums:
    up = (-value+mean)
    upp = upp + up*up
    down = len(nums)
stDv = math.sqrt(upp/down)
print("The average is:","{0:0.2f}".format(mean))
print("The std deviation is:","{0:0.2f}".format(stDv))
count=0


#def main:
    # dict= {...}
    
    #num = calextract(dict)
    #sum = calsum(nums)
    #mean = calmean(nums,sum)
    #std = calstd(nums,mean,sum)
    #check(dict, mean)
#main()

if(len(c)>2):
    print("List of students who need to see an advisor:")
for i in b:
    c.append(i)
    for j in c:
        if j == c[len(c)-1]:
            d = j
        else:
            d = j[:-1]
            

    #spliting whats in the list d
    x,y = d.split(",")
    if(int(y)<mean):

        print(x)
        

