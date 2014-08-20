#Khyati Jinerdeb
#Assignment 6
#25 April 2014
#program to right align a list of strings right aligned with the longest string

#defines a list

namesList=[]

#prompts user to input a list of strings that has "DONE" as sentinel

name=input("Enter strings (end with DONE):\n")

#to define "DONE" to be the sentinel value
while name!="DONE":
    namesList.append(name)    #adds next name to the list
    name=input()
    
right_aligned_list=[]           #defines the right aligned list
print("\nRight-aligned list:")  #prints the list of strings in a right aligned format

#to find the name with the maximum length

maximum=0
for i in namesList:   #to find the word with the maximium length
    x=len(i)
    if x>maximum:
        maximum=x    #if another maximum is found, x taks this value.
        
#to find how many spaces are required to make the word right justified
for i in namesList:
    print(" "*(maximum-len(i)),i,sep="")   
    
    
    
    
    
    
          
    
    
               
          
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
