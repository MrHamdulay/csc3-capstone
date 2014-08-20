"""This program tekes in a list of marks and outputs the a histogram representation of the marks
Hebert Tema
21-04-2014"""

#prompts the user to unput a list of marks
marks=input("Enter a space-separated list of marks:\n")

#split the string enter into a list and create a dictionary with category(key) and range(value)
marks_list=marks.split()
ordered_l=["1","2+","2-","3","F"]
dictionary={}
category={"1":"j>=75","2+":"75>j>=70","2-":"70>j>=60","3":"60>j>=50","F":"j<50"}

#count number of scores in each category
for i in category:
    for j in marks_list:
        j=eval(j)
        value=category[i]
        if eval(value):
            if i in dictionary:
                dictionary[i]+=1
                continue
            else: dictionary[i]=1


#output the histogram representation
for i in ordered_l:
    quantity=dictionary.get(i, 0)
    print("{0:<2}".format(i), "|", "X"*quantity, sep="")
