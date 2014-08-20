# program that outputs a histogram representation of a list of marks
# khadeejah omar
# 21 april 2014

marks = input("Enter a space-separated list of marks: \n")
first = 0
upper_second = 0
lower_second = 0
third = 0
fail = 0

# determine the amount of marks in each category - counter
for mark in marks.split() : 
    mark = eval(mark)
    if mark >= 75 :
        first += 1
    if 75 > mark >= 70 :
        upper_second += 1
    if 70 > mark >= 60 :
        lower_second += 1
    if 60 > mark >= 50 :
        third += 1
    if mark < 50 :
        fail += 1
        
# store counter in a list
counter_list = []
counter_list.append(first)
counter_list.append(upper_second)
counter_list.append(lower_second)
counter_list.append(third)
counter_list.append(fail)

# draw the bars for each mark
histogram = []
for count in counter_list :
    bars = "|" + "X" * count
    histogram.append(bars)

    
labels = ["1 ", "2+", "2-", "3 ", "F "] # stored labels for each category

# draw each bar in its labelled category
labelled_histogram = []
bar_index = 0
for alabel in labels :
    print(alabel + histogram[bar_index])
    bar_index += 1