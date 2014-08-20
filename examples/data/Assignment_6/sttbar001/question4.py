"""program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT:
20/04/2014
barak setton STTBAR001"""
marklist = []
markcount=[0]*5
count =0
marks =input("Enter a space-separated list of marks: \n")
marklist = marks.split(" ")

for l in marklist:
    if eval(l)<50:
        markcount[0] += 1
    elif 50<= eval(l) < 60:
        markcount[1] += 1
    elif 60<= eval(l) < 70:
        markcount[2] += 1
    elif 70 <= eval(l) < 75:
        markcount[3] += 1
    elif 75<=eval(l):
        markcount[4] += 1


print("1 |"+"X"*markcount[4])
print("2+|"+"X"*markcount[3])
print("2-|"+"X"*markcount[2])
print("3 |"+"X"*markcount[1])
print("F |"+"X"*markcount[0])