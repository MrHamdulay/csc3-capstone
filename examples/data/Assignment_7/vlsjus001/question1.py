#assignment 7 question 1
#creating a dictionary
#justin valsecchi
#2014/05/02

dictn=[]
strings= input("Enter strings (end with DONE):\n")
while strings != 'DONE':
        dictn.append(strings)
        strings = input("")
  

uniq = []
for i in dictn:
        if not i in uniq:
                uniq.append(i)
            


print("\nUnique list:")
for x in uniq:
        print(x)
    


    
        
    