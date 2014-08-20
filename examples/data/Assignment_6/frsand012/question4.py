def histogram():
    histogram = input("Enter a space-seperated list of marks: \n")

    # Allows program to recognise inputs into a list by putting a space between them
    list_marks = histogram.split
    
    # This will convert the strings into a list of numbers in order to use format
    for j in range(len(list_marks)): 
        list_marks[j] = eval(list_marks[j]) # Changes from string to number
        
    # Create a dictionary as values have already been give for the marks
    # Makes it easier than working with variables in format
    
    Repetitions = {"1 ": 0, "2+": 0, "2-": 0, "3 ": 0, "F ": 0} # Start from 0
    
    # Use if and elif to separate various marks into categories
    
    for histogram in list_marks:
        if mark >=75:
            repetition["1 "] +=1 # Adds 1 every repitition
        elif 70 <=histogram<75:
            repetition["2+"] +=1
        elif 60 <=histogram< 70:
            repetition["2-"] +=1
        elif 50 <=histogram< 60:
            repetition["3 "] +=1
        elif histogram<50:
            repetition["F "] +=1        
    
    # Now print the repetition with the marks
    
    print("1 |", repetition["1 "] * "X", sep = "")
    print("2+|", repetition["2+"] * "X", sep = "")
    print("2-|", repetition["2-"] * "X", sep = "")
    print("3 |", repetition["3 "] * "X", sep = "")
    print("F |", repetition["F "] * "X", sep = "")

histogram()