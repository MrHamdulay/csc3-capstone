#Author:Percival Munhuwaani
#Program:A program that creates a histogram according the mark categories
#Date:24/04/2014
def main():
    mark_list=input("Enter a space-separated list of marks:\n").split()
    list1=[] #creating an empty list to store the marks in each category
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    for i in mark_list:
        if eval(i)<50:  #putting the marks into the first category
            list1.append(i)  #adding the marks to the list
        elif 50<=eval(i)<60: #putting the marks into the second category
            list2.append(i)  #adding the marks to the list
        elif 60<=eval(i)<70: #putting the marks into the third category
            list3.append(i)  #adding the marks to the list
        elif 70<=eval(i)<75: #putting the marks into the fourth category
            list4.append(i)  #adding the marks to the list
        else:
            list5.append(i)  #adding the marks to the list5
    print("1 |"+len(list5)*"X")
    print("2+|"+len(list4)*"X")
    print("2-|"+len(list3)*"X")
    print("3 |"+len(list2)*"X")
    print("F |"+len(list1)*"X")
main()