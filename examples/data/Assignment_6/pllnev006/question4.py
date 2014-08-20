#Program to create a histogram of marks
#Nevarr Pillay - PLLNEV006
#22 April 2014

marks = [["1",0],["2+",0],["2-",0],["3",0],["F",0]] #2D array with all possible mark classes

def readMarks(): #Reads in the marks and increases the appropriate classes
    list_marks = input("Enter a space-separated list of marks:\n")
    for mark in list_marks.split(" "):
        mark = eval(mark)
        if mark < 50:
            marks[4][1] += 1
        elif 50 <= mark < 60:
            marks[3][1] += 1
        elif 60 <= mark < 70:
            marks[2][1] += 1
        elif 70 <= mark < 75:
            marks[1][1] += 1
        else:
            marks[0][1] += 1
            
def histogram(): #Creates histogram using the category and number of marks in each category
    catOut = "{0:<2}|"
    for item in marks:
        category = item[0]
        numMarks = item[1]
        print(catOut.format(category),"X"*numMarks,sep="")
        
def main():
    readMarks()
    histogram()
    
if __name__ == "__main__":
    main()