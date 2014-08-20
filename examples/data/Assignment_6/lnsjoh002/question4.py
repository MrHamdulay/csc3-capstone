"""Program to make a histogram from a set of marks
JP Lanser
20 April 2014"""

#prompt the user to input marks, split the string into a list straight away

marks = input("Enter a space-separated list of marks:\n").split(" ")

# Create a dictionary to store the number the number of firsts, upper seconds and so on. Set them all to value zero initially

dictionary = { "1" :0 , "2+": 0 ,"2-":0, "3":0 , "F":0}

#loop through the list provided by the user and add to the dictionary

for i in marks :
    mark = eval(i)   #evaluate i so that the mark can be categorized correctly
    
    
    #Now put the mark in  the relevant category and add it to the dictionary
    if mark >= 75:
        dictionary["1"] +=1
    
    elif 70<= mark <75:
        dictionary["2+"] +=1
        
    elif 60<= mark <70:
        dictionary["2-"] += 1
    
    elif 50 <= mark <60:
        dictionary["3"]+=1
        
    elif mark < 50:
        dictionary["F"] +=1
        

#Create a variable for each category to store the number of "X" required on histogram

firsts = "X" * dictionary["1"]
upper_seconds = "X" * dictionary["2+"]
lower_seconds = "X" * dictionary["2-"]
thirds = "X" * dictionary["3"]
fails = "X" * dictionary["F"]

#Now print histogram as required per sample I/O

print("1 |", firsts, sep="")

print("2+|", upper_seconds, sep="")

print("2-|", lower_seconds, sep="")

print("3 |", thirds, sep="")

print("F |", fails, sep="")



