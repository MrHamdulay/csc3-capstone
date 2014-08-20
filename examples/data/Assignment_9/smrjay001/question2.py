"""
Assignment 9 - Question 2
Program to format the length of each line in a text file
Jayan Smart
15 May 2014
"""



def openf(file):             #Open the file
    with open(file) as f:
        lines = f.read()
            
    return lines

def splitline(text):        #split into a 2D array of lines in each paragraph
    par = text.split("\n\n")
    #print(par)
    for i in range(len(par)):
        par[i] = par[i].split()
    #print(par)
    return par   

def countlen(text, count, lenth, out):   #Count and split into lines of set length
    if text == []:
        return print("\n", file = out)
    
    count += len(text[0])
    count += 1 #add one for the space
           
    if count <=lenth:
        word = text[0]
        print(word, end = ' ', file = out)
        return countlen(text[1:], count, lenth, out)
    else:
        print('', file = out)
        return countlen(text, 0, lenth, out)                
def main():
    infile = input("Enter the input filename:\n")
    outfile = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))
    openf(infile)
    line = openf(infile)
    text = splitline(line)
    with open(outfile, 'w') as out:
        for i in range(len(text)):
            countlen(text[i], 0, width, out)
            
if __name__ == "__main__":
    main()
