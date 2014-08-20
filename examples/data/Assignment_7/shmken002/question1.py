"""returning list of strings without duplicates
ringo shima
29/04/14"""

def main():
    list1 = [] #initiate empty list
    list2 = [] #initiate list without dups
    
    word = print("Enter strings (end with DONE):")
    while word != "DONE": #make end point
        word = input()
        
        list1.append(word) #keep adding words to list
        for word in list1: 
            if not word in list2: #checking if word occurs in 2nd list. If not, add
                list2.append(word)
            
    list2.remove("DONE") 
    print()
    print("Unique list:")
    for i in list2: #print each indexed item in string
        print(i)
    
    
   
        
main()