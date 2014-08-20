"""program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks
peter m muriuki"""

#get the list of marks and add them into an array
marks_str=input("Enter a space-separated list of marks:\n")
marks=marks_str.split(" ")
counter={'w':0,'x':0,'y':0,'z':0,'f':0} #initialise a counter (dictionary)

#sort the marks into different categories and count occurencies of each different category,storing them into the counter
for item in marks:
    item=int(item)
    if item >=75:
        counter['w'] +=1
    elif 70<=item<75:
        counter['x'] +=1
    elif 60<=item<70:
        counter['y'] +=1
    elif 50<=item<60:
        counter['z'] +=1
    elif item<50:
        counter['f'] +=1
        
#print out the different counts for each category of marks in a histogram format
print ("1 |","X"*counter['w'],sep="")
print ("2+|","X"*counter['x'],sep="")
print ("2-|","X"*counter['y'],sep="")
print ("3 |","X"*counter['z'],sep="")
print ("F |","X"*counter['f'],sep="")
        