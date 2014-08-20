'''program to compute a graph for the spread of marks in class
Wandile Khowa
20-04-2014
'''
ans = input("Enter a space-separated list of marks:\n")
ans_n = ans.split() #splits the marks into a list
first = 0
upper_s = 0
lower_s = 0
third = 0
fail = 0
for i in ans_n:
    if eval(i) >= 75:   #counts how many learners' marks fall in this category
        first += 1
    elif eval(i) >= 70 and eval(i) < 75:    #counts how many learners' marks fall in this category 
        upper_s += 1
    elif eval(i) >= 60 and eval(i) < 70:    #counts how many learners' marks fall in this category
        lower_s += 1
    elif eval(i) >= 50 and eval(i) < 60:    #counts how many learners' marks fall in this category
        third += 1
    elif eval(i) < 50:  #counts how many learners' marks fall in this category
        fail += 1
        
print("1 ", "|"+(first*"X"), sep="")    #prints the graph with horizontal bars
print("2+", "|"+(upper_s*"X"), sep="")
print("2-", "|"+(lower_s*"X"), sep="")
print("3 ", "|"+(third*"X"), sep="")
print("F ", "|"+(fail*"X"), sep="")
    
