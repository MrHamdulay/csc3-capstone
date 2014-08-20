# Assignment 6 - Question 4
# A program that takes a list of marks and outputs them in histogram representation according to categories
# Written by: Laene van Niekerk
# VNKLAE001

marks = input("Enter a space-separated list of marks:\n")
string_list = marks.split(" ")  # Creates a list of numbers represented as strings
num_list = []

for i in string_list:   # Converts the string entered by the user into a list of numbers
    x = eval(i)
    num_list.append(x)
    
categories = ["1","2+","2-","3","F"]
cat_1 = 0
cat_2_plus = 0
cat_2_minus = 0
cat_3 = 0
cat_F = 0
    
for i in num_list:  # Counts the number of marks that fall into the categories
    if i >= 75:
        cat_1 = cat_1 + 1
    elif 70 <= i < 75:
        cat_2_plus = cat_2_plus + 1
    elif 60 <= i < 70:
        cat_2_minus = cat_2_minus + 1
    elif 50 <= i < 60:
        cat_3 = cat_3 + 1
    else:
        cat_F = cat_F + 1
        
counts = [cat_1, cat_2_plus, cat_2_minus, cat_3, cat_F]
pos = 0

for i in categories:
    tally = counts[pos]
    tally = "X"*tally
    tally = str(tally)
    tally = "|" + tally
    form = "{:<2}{:>0}".format(i, tally)
    print(form)
    pos = pos + 1
        

        
    
