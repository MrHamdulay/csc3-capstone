"""Making a histogram from a set of given marks
By Daniel Newton
19/04/14"""

#Default string parts of the histogram created to be added to.
first='1 |'
Up2nd='2+|'
Lo2nd='2-|'
third='3 |'
fail='F |'

marks=input("Enter a space-separated list of marks:\n")     #Prompts use input of however many marks they choose separated by a space

for mark in marks.split(' '):   #Splits the list of marks, evaluating each mark and adding an 'X' character to the string on the histogram that applies to that mark.
    mark=eval(mark)
    
    if mark>=75:
        first+='X'
        
    elif mark>=70:
        Up2nd+='X'
        
    elif mark>=60:
        Lo2nd+='X'
        
    elif mark>=50:
        third+='X'
        
    elif mark>=0:
        fail+='X'

print(first,Up2nd,Lo2nd,third,fail,sep="\n")