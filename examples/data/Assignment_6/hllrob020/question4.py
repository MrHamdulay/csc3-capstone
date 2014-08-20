mark_list = [] #empty list for marks

marks = input('Enter a space-separated list of marks:\n')
marks_split = marks.split() #to split single string entry into different 'mark' stirngs
for i in range(len(marks_split)): #iterates through length of mark list
    mark_list.append(eval(marks_split[i])) #appends evaluated string as number into mark list

first = 0 
up_second = 0
low_second = 0
third = 0
fail = 0 #setting all mark code counts to 0
for mark in mark_list: #iterates through numbers in mark list
    if 75 <= mark <= 100:
        first += 1 #if mark between 75 and 100, adds one to first code
    elif mark >= 70:
        up_second += 1 #mark greater than 70, adds one to upper second code
    elif mark >= 60:
        low_second += 1 #mark greater than 60, adds one to lower second code
    elif mark >= 50:
        third += 1 #mark greater than 50, adds one to third code
    elif 0 <= mark < 50:
        fail += 1 #mark between 0 and 50, adds one to fail code

symb = 'X'
print('1 |',first*symb,sep = '')
print('2+|',up_second*symb,sep ='')
print('2-|',low_second*symb,sep ='')
print('3 |',third*symb,sep = '')
print('F |',fail*symb,sep = '') #prints number X's times the mark codes
        
    