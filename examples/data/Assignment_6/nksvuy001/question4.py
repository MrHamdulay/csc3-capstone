"""program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
vuyolwethu nkosi
23 april 2014"""

#get list of marks from user
mark=input("Enter a space-separated list of marks:\n")
mark=mark.split() #split into list
#create empty list
M=[]
#create list
for j in mark:
    M.append(eval(j)) #adding to list the numbers
    
#create counter variable with 5 spaces to store counts in
counter=["","","","",""]
for i in M: #going through list M
    #if it finds the number within the range, it should add X to that space position allocated
    if 0<=i<50: 
        counter[4] = counter[4] + "X" #position 4 print an X
    elif 50<=i<60:
        counter[3]= counter[3] + "X" #position 3 print an X
    elif 60<=i<70:
        counter[2]= counter[2] + "X" #position 2 print an X
    elif 70<=i<75:
        counter[1]= counter[1] + "X" #position 1 print an X
    else:
        counter[0]=counter[0] + "X" #position 0 print an X
#print results    
print("1 |",counter[0],sep="")
print("2+|",counter[1],sep="")
print("2-|",counter[2],sep="")
print("3 |",counter[3],sep="")
print("F |",counter[4],sep="")



        

