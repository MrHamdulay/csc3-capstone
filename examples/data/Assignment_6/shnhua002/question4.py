#Charlie Shang
#SHNHUA002
#Assignment 6 Q4

def classify(arr, count):  #counts the number of marks in each category
    for i in range(0,len(arr),1):  
        if arr[i] < 50:
            count[0] += 1
        elif arr[i]<60:
            count[1] += 1
        elif arr[i] < 70:
            count[2] += 1
        elif arr[i] < 75:
            count[3] += 1
        else:
            count[4] += 1
    return arr, count

arr = (input("Enter a space-separated list of marks:\n").rstrip()).split(' ')

for i in range(0,len(arr),1):
    arr[i] = int(arr[i])

count = [0,0,0,0,0] # empty list of mark categories count, [F,3,2-,2+,1]

arr, count = classify(arr, count) 

#printing the histogram
print("1 |"+"X"*count[4])
print("2+|"+"X"*count[3])
print("2-|"+'X'*count[2])
print("3 |"+'X'*count[1])
print("F |"+'X'*count[0])

