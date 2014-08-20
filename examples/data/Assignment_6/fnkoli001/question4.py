#Get input
inp_marks = input("Enter a space-separated list of marks:\n")

marks = [eval(i) for i in inp_marks.split(" ")]

fst = ""
upeer_snd = ""
lower_snd = ""
trd = ""
fail = ""

for mark in marks:
    if mark > 100:
        print("ERROR")
    elif mark >= 75:
        fst += "X"
    elif mark >= 70:
        upeer_snd += "X"
    elif mark >= 60:
        lower_snd += "X"
    elif mark >= 50:
        trd += "X"
    else:
        fail += "X"

print("1 |" + fst)
print("2+|" + upeer_snd)
print("2-|" + lower_snd)
print("3 |" + trd)
print("F |" + fail)