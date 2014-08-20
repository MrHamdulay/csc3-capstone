#CSC ass.6 Q4 mark classification
#Kavir Ranchod rnckav001
#23/04/2014

#Fetch all marks
marks=input("Enter a space-separated list of marks:\n")
#split string into a list
mark=marks.split(" ")
#initiate counting variables
fail=0
third=0
lowersecond=0
uppersecond=0
first=0
#checks to classify each mark under a category
for i in mark:
    if 0 <= eval(i) < 50:
        fail+=1
    elif 50 <= eval(i) < 60:
        third+=1
    elif 60 <= eval(i) < 70:
        lowersecond+=1
    elif 70 <= eval(i) < 75:
        uppersecond+=1
    elif 75 <= eval(i) <= 100:
        first+=1
#print out each bar of the "histogram"
print("1 |"+"X"*first)
print("2+|"+"X"*uppersecond)
print("2-|"+"X"*lowersecond)
print("3 |"+"X"*third)
print("F |"+"X"*fail)