"""question 4
20 April 2014
by Jonathan Ovadia"""
def main():
    marks = input("Enter a space-separated list of marks:\n").split(" ")
    print(histogram(marks))

def histogram(l):
    fail = "F |"
    third = "3 |"
    lower_second = "2-|"
    upper_second = "2+|"
    first = "1 |"
    for i in range(len(l)):
        if eval(l[i]) < 50 :
            fail+="X"
        elif eval(l[i]) > 49 and  eval(l[i]) < 60:
            third +="X"
        elif eval(l[i]) > 59 and  eval(l[i]) < 70:
            lower_second +="X"
        elif eval(l[i]) > 69 and  eval(l[i]) < 75:
            upper_second +="X"
        else:
            first+="X"
    return first + "\n" + upper_second + "\n" + lower_second + "\n" +third + "\n" + fail
main()