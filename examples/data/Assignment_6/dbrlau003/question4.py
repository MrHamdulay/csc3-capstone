#Lauren de Bruyn
#Program that outputs a histogram representation of the marks according to the mark categories at UCT
#22 April 2014

#ask user to input list of marks
marks= input("Enter a space-separated list of marks: \n")
list_marks= marks.split(" ")

#create empty lists for each mark catergory
faillist=[]
thirdlist=[]
lowersecondlist=[]
uppersecondlist=[]
firstlist=[]

#sort marks into correct categories and add the mark in corresponding list
for mark in list_marks:
    if int(mark)<50:
        faillist.append(mark)
    elif 50<=int(mark)<60:
        thirdlist.append(mark)
    elif 60<=int(mark)<70:
        lowersecondlist.append(mark)
    elif 70<=int(mark)<75:
        uppersecondlist.append(mark)
    else:
        firstlist.append(mark)

#print histogram of marks
print("1 |", len(firstlist)*'X',sep='')
print("2+|", len(uppersecondlist)*'X',sep='')
print("2-|", len(lowersecondlist)*'X',sep='')
print("3 |", len(thirdlist)*'X',sep='')
print("F |", len(faillist)*'X',sep='')

        

