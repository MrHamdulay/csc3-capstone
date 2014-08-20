"""Program doing a histogram
Khanyisile Morudu
20 April 2014"""

#initializing an array with a list corresponding to it
arr1 = []
arr2_hi = []
arr2_lo = []
arr3 = []
arrF = []

#input
marks = input("Enter a space-separated list of marks:\n")

#seperating the list
marks_all = marks.split(" ")

#classifying each mark
for i in range(len(marks_all)):
    if int(marks_all[i]) < 50:
        arrF.append(1)
    if ((int(marks_all[i]) >= 50) and (int(marks_all[i]) < 60)) :
        arr3.append(1)        
    if (int(marks_all[i]) >= 60) and (int(marks_all[i]) < 70) :
        arr2_lo.append(1)
    if (int(marks_all[i]) >= 70) and (int(marks_all[i]) < 75) :
        arr2_hi.append(1)
    if (int(marks_all[i]) >= 75):
        arr1.insert(len(arr1), 1)
        
    
#printing
a = "{0:>2}"
print("1 |" + "X" * len(arr1))
print("2+|" + "X" * len(arr2_hi))
print("2-|" + "X" * len(arr2_lo))
print("3 |" + "X" * len(arr3))
print("F |" + "X" * len(arrF))

