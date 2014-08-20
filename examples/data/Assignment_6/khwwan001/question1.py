'''program to allow user to type in a list of names and can exit with the sentinel 'DONE'
Wandile Khowa
20-04-2014
'''
def names(a):
    ques = a
    global max_str
    list_n = [] #creates an empty list
    max_str = len(ques)     #makes the current length of string the maximum  
    while ques != "DONE":   #creates a sentinel "DONE" 
        list_n.append(ques) #adds word in list 'list_n'
        ques = input("")
        if len(ques) >= max_str:    #checks to see if current string is longer than previous one, and set max accordingly
            max_str = len(ques)
        else:
            max_str = max_str 
            
    return list_n
    
def main():
    ques = input("Enter strings (end with DONE): \n") 
    x = names(ques)
    print("\nRight-aligned list:")
    for i in x:
        print(i.rjust(max_str)) # prints the list right justified with a width corresponding to the maximum length of a word in list_n    
        
if __name__=='__main__':
    main()
    
    
    
