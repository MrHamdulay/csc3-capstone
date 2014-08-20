#VRMNIC005
#assignment 6 question 4

# splits input into list of integers
marks = list(map(int, input("Enter a space-separated list of marks: \n").split())) 

fail = 0
third = 0
second_lower = 0
second_upper = 0
first = 0

for i in marks:  
    if i <50:
        fail += 1

    elif 50 <= i < 60:
        third += 1

    elif  60 <= i < 70:
        second_lower += 1

    elif 70 <= i < 75:
        second_upper += 1

    else:
        first += 1

print("1 |", "X"*first, sep ="")
print("2+|", "X"*second_upper, sep ="")
print("2-|", "X"*second_lower, sep ="")
print("3 |", "X"*third, sep ="")
print("F |", "X"*fail, sep ="")
