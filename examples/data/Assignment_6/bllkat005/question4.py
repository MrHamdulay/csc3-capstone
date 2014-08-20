# Kate Bell
# BLLKAT005
# 22 April 2014 

# Input list of marks from user
marks_array = input("Enter a space-separated list of marks:\n").split(" ")

# Loop through array to count the number in each mark category in the dictionary marks_dic
marks_dic ={'1':0, '2+':0, '2-':0, '3':0, 'F':0}
for i in range(len(marks_array)):
    if eval(marks_array[i]) < 50:
        marks_dic['F'] += 1
    elif 50 <= eval(marks_array[i]) < 60:
        marks_dic['3'] += 1
    elif 60 <= eval(marks_array[i]) < 70:
        marks_dic['2-'] += 1
    elif 70 <= eval(marks_array[i]) < 75:
        marks_dic['2+'] += 1
    elif eval(marks_array[i]) >= 75:
        marks_dic['1'] += 1

print("1 |","X"*marks_dic['1'],sep="")
print("2+|","X"*marks_dic['2+'],sep="")
print("2-|","X"*marks_dic['2-'],sep="")
print("3 |","X"*marks_dic['3'],sep="")
print("F |","X"*marks_dic['F'],sep="")