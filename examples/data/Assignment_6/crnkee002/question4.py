"""A6Q4 - Mark Histogram
CRNKEE002
21/4/2013"""

markCounts = [["1 |", 0],["2+|", 0],["2-|", 0],["3 |", 0],["F |", 0]]

def main():
    get_marks()
    print_histogram(markCounts)
    
def get_marks():
    global markCounts
    markstr = input("Enter a space-separated list of marks:\n")
    ArrayMarks = markstr.split(" ")
    for i in range(len(ArrayMarks)):
        if int(ArrayMarks[i]) >= 75:
            markCounts[0][1] += 1
        elif 70 <= int(ArrayMarks[i]) < 75:
            markCounts[1][1] += 1
        elif 60 <= int(ArrayMarks[i]) < 70:
            markCounts[2][1] += 1
        elif 50 <= int(ArrayMarks[i]) < 60:
            markCounts[3][1] += 1
        else:
            markCounts[4][1] += 1
            
def print_histogram(array):
    for i in range(5):
        print(markCounts[i][0], end="")
        for j in range(markCounts[i][1]):
            print("X", end="")
        print("")    
if __name__ == "__main__":
    main()