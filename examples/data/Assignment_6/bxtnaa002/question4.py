# question4.py
# author: bxtnaa002

num_str = input("Enter a space-separated list of marks:\n")
numbers = num_str.split(" ")

#create separate lists which will contain the X for the count in each range
bars1=[]
bars2up=[]
bars2low=[]
bars3=[]
barsf=[]

X = 'X'
for number in numbers: #go through all the numbers in the original list inputed
    if int(number) < 50: #make the number an integer to evaluate its size in relation to the ranges given
        barsf.append(X) 
    elif 50 <= int(number) < 60:
        bars3.append(X)              #add X for every number in numbers that falls within the given range
    elif 60 <= int(number) < 70:
        bars2low.append(X)
    elif 70 <= int(number) < 75:
        bars2up.append(X)
    elif int(number) >= 75:
        bars1.append(X)

# print the histogram by joining the X in each list with an empty string so that they can be directly next to each other
        
print("1 |"+"".join(bars1))
print("2+|"+"".join(bars2up))
print("2-|"+"".join(bars2low))
print("3 |"+"".join(bars3))
print("F |"+"".join(barsf))
        