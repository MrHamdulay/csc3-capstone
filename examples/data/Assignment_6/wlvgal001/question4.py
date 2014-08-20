#Question 4: UCT mark histogram
#Galya Wolov
#24 April 2014

#get a string and make into an array
marks= input("Enter a space-separated list of marks:\n")
listedmarks=marks.split(' ')


fail= []
third=[]
lowersecond= []
uppersecond= []
first=[]

#make items in array integers and cateogrorise according to UCT 
for item in listedmarks:
    integeritem=int(item)
    if integeritem < 50:
        fail.append(integeritem)
    elif 50 <= integeritem <60:
        third.append(integeritem)
    elif 60 <= integeritem < 70:
        lowersecond.append(integeritem)
    elif 70 <= integeritem < 75:
        uppersecond.append(integeritem)
    else:
        first.append(integeritem)

#prints histogram
print("1 |"+("X"*len(first)))
print("2+|"+("X"*len(uppersecond)))
print("2-|"+("X"*len(lowersecond)))
print("3 |"+("X"*len(third)))
print("F |"+("X"*len(fail)))


