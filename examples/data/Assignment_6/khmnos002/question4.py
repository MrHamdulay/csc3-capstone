"""program that outputs histogram of marks 
nosipho khumalo
19 April 2014"""

def main():
    #inputing marks
    marks = input("Enter a space-separated list of marks: \n")
    marks = marks.split(" ")
   
    #initiating counters for each category
    countf = 0
    count3rd = 0
    countlow = 0
    countup = 0
    count1st = 0
    
    #counting number of marks in each category
    for i in range(len(marks)):
        if int(marks[i]) < 50:
            countf += 1
        elif int(marks[i]) < 60:
            count3rd += 1
        elif int(marks[i]) < 70:
            countlow += 1
        elif int(marks[i]) < 75:
            countup += 1
        else:
            count1st += 1
    
    #printing histogram
    print("1 |", "X" * count1st, sep = "")
    print("2+|", "X" * countup, sep = "")
    print("2-|", "X" * countlow, sep = "")
    print("3 |", "X" * count3rd, sep = "")
    print("F |", "X" * countf, sep = "")
main()