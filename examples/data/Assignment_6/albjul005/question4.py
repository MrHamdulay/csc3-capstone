"""Program for lists3 - histogram
Julian Albert
ALBJUL005
2014-04-23"""

#create lists for 5 sets of marks
list_1st = []
list_upper2 = []
list_lower2 = []
list_3 = []
list_Fail = []

#get list of marks from user and convert to a list
def get_list():
    string = input("Enter a space-separated list of marks:\n")
    all_marks = string.split(" ")
    return all_marks

#sorts all_marks into grades
def data():
    for i in get_list():
        if i.isdigit():
            i = eval(i) #integer check
            if 0 <= i < 50:
                list_Fail.append(i) #appends mark to fail column
            elif i < 60:
                list_3.append(i) #appends mark to 3 column
            elif i < 70:
                list_lower2.append(i) #appends mark to 2- column
            elif i < 75:
                list_upper2.append(i) #appends mark to 2+ column
            elif i <= 100:
                list_1st.append(i) #appends mark to 1 column

#print graph of (|)[X*n]
def histogram():
    data()
    print("1 |"+"X"*len(list_1st))
    print("2+|"+"X"*len(list_upper2))
    print("2-|"+"X"*len(list_lower2))
    print("3 |"+"X"*len(list_3))
    print("F |"+"X"*len(list_Fail))
       
histogram()