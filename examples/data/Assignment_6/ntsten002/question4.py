#question4
#Tendani Netshitenzhe
#25 April 2014

#Get list of marks
list_marks = input("Enter a space-separated list of marks:\n").split(' ')

#assigning variables to each mark category
first = "1 |"
third = "3 |"
low_second = "2-|"
high_second = "2+|"
fail = "F |"

#Determine in which group each mark belongs and place an X
for k in range(len(list_marks)):
    if int(list_marks[k]) < 50:
        fail += "X"
    elif 50 <= int(list_marks[k]) < 60:
        third += "X"
    elif 60 <= int(list_marks[k]) < 70:
        low_second += "X"
    elif 70 <= int(list_marks[k]) < 75:
        high_second += "X"
    else:
        first += "X"
        
#Printing histogram
print(first+"\n"+high_second+"\n"+low_second+"\n"+third+"\n"+fail)