# get a input from user
marks = input ("Enter a space-separated list of marks:\n")

# separate into list of words
arrMarks = marks.split (" ")

# start with zero counters
counter= {"1":0, "2+":0, "2-":0, "3":0, "F":0}

# count words and add new words as they are encountered
for mark in arrMarks:
    if eval(mark) >= 75:
        counter["1"] +=1
    elif eval(mark) >= 70:
        counter["2+"]+=1
    elif eval(mark) >= 60:
        counter["2-"]+=1 
    elif eval(mark) >= 50:
        counter["3"]+=1 
    else:
        counter["F"]+=1
    
# print out counters
print("1 |" + ("X"*counter["1"]))
print("2+|" + ("X"*counter["2+"]))
print("2-|" + ("X"*counter["2-"]))
print("3 |" + ("X"*counter["3"]))
print("F |" + ("X"*counter["F"]))