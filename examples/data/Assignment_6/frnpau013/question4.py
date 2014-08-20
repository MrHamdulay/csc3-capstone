"""histogram of marks by UCT mark symbols"""

# get marks, evaluate from str to mathematical sequence and convert to list"
marklist = list(eval(input("Enter a space-separated list of marks:\n").replace(" ", ", ")))

# convert to dictionary of marks categorized by UCT symbols, named histogram
histogram = {"F ":0, "3 ":0, "2-":0, "2+":0, "1 ":0}

for i in marklist:
    if i < 50:
        histogram["F "] += 1
    elif i <60:
        histogram["3 "] += 1
    elif i < 70:
        histogram["2-"] += 1
    elif i < 75:
        histogram["2+"] += 1
    else:
        histogram["1 "] += 1

gradelist = sorted(histogram) # created a sorted list of mark symbols

# output
for i in gradelist:
    print(i, "|", "X" * histogram[i], sep = "")