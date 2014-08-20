"""function to recall
Mr Luci Ntanjana
01 April 2014"""

def print_square():
  
 print("*****")
 print("*   *")
 print("*   *")
 print("*   *")
 print("*****") 
 
def print_rectangle(x,y):
    print("*"*int(x))
    for i in range(int(y)-2):
        k=int(x)-2
        print("*", " "*k, "*",sep="")
    print("*"*int(x))
    
    
def get_rectangle(x,y):

    c=int(x)-2
    k="*"*int(x)+("\n")
    for i in range(int(y)-2):
        k=k+"*"+ " "*c+ "*"+("\n")
    k=k+"*"*int(x)
    return(k)
# test program for box drawer

import boxes

choice = input ("Choose test:\n")
action = choice[:1]
if action == 'a':
   boxes.print_square ()
elif action == 'b':
   width, height = map (int, choice[2:].split(" "))
   print ("calling function")
   boxes.print_rectangle (width, height)
   print ("called function")
elif action == 'c':
   width, height = map (int, choice[2:].split(" "))
   print ("calling function")
   figure = boxes.get_rectangle (width, height)
   print ("called function")
   print (figure)   
 