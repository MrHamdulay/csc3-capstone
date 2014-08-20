#danson Masuka
#listing marks in a histogram
#23 april 2014

marks = []
marksinput = input ("Enter a space-separated list of marks:\n")

marks = marksinput.split()
first = 0
second1 = 0
second2 = 0
third = 0
fail = 0
for i in marks:
    if 75<= int(i) <=100:
        first += 1
    elif int(i) >= 70:
        second1 += 1
    elif int(i) >= 60:
        second2 += 1
    elif int(i) >= 50:
        third += 1
    elif int(i) < 50:
        fail += 1
print("1 |"+"X"*first)
print("2+|"+"X"*second1)
print("2-|"+"X"*second2)
print("3 |"+"X"*third)
print("F |"+"X"*fail)