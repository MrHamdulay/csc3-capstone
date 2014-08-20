"""A program to rank a list of marks according to UCT mark catagories
by Jeremy Smith
21 April 2014"""

#create a dictionary of the mark catagories
mark_catagory = {'1':"", '2+':"", '2-':"",'3':"", 'F':""}
mark_catagory_list = ['1','2+','2-','3','F']

#input a list of marks
mark_string = input("Enter a space-separated list of marks:\n")
mark_list = mark_string.split(" ")

#for marks that pertain to a catagory assign and X to the value of the dictionary key
for i in mark_list:
    if eval(i) >= 75:
        mark_catagory['1'] += 'X'
    elif eval(i) >= 70:
        mark_catagory['2+'] += 'X'
    elif eval(i) >= 60:
        mark_catagory['2-'] += 'X'
    elif eval(i) >= 50:
        mark_catagory['3'] += 'X'
    else:
        mark_catagory['F'] += 'X'

#output the list of mark catagories with the number of relevant mark scores indicated by 'X'
for i in mark_catagory_list:
    align = "{0:<2}"
    print(align.format(i),'|',mark_catagory[i] ,sep='')