#takes a list of words and returned a kist of the words right aligned
#Dacod Magagula
#22 April 2014

def length():
    #Get the names and create an empty list
    name_l=[]
    names=input("Enter strings (end with DONE):\n")
    namelength=[]
    #get more names untill the user types in 'DONE'
    while names != "DONE":
        name_l.append(names)
        names=input("")
        if names=="DONE":
            break
    print()
    print("Right-aligned list:")
    #interate through each word and get it's length and add it to the list
    for word in name_l:
       
        namelength.append(len(word))
    #find the maximum of the lengths of the words      
        maximum_l=max(namelength)
    #Iterate through the list and print each word and right align it according to the longest word i the list
    for word in name_l:
        word_length=len(word)
        print(' '*(maximum_l-word_length),word,sep='')
           
        

    #print("maximum_l=",maximum_l)    
    #print(namelength)    
    #print(name_l)
        
    
   
length()