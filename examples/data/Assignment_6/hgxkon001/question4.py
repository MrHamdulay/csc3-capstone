#Konrad Hugo
#question4
#25 April 2014

#lists that will contain frequencies of different categories of marks
list1 = []
list2upper = []
list2lower = []
list3 = []
listf = []

#converts marks from user input into list
def list_converter():
    string = input("Enter a space-separated list of marks:\n")
    marks = string.split(" ")
    return marks

#s
def information():
    for i in list_converter():
        if i.isdigit(): #only performs looop if characters are all digits
            i = eval(i) 
            if 0 <= i < 50:
                listf.append(i) 
            elif 50 <= i < 60:
                list3.append(i) 
            elif 60 <= i < 70:
                list2lower.append(i) #appends to this category
            elif 70 <= i < 75:
                list2upper.append(i) #appends to this category
            elif 75 <= i <= 100:
                list1.append(i) #appends to top achievers column

#print graph of (|)[X*n]
def graph():
    information()
    print("1 |"+"X"*len(list1))
    print("2+|"+"X"*len(list2upper))
    print("2-|"+"X"*len(list2lower))
    print("3 |"+"X"*len(list3))
    print("F |"+"X"*len(listf))
       
graph()