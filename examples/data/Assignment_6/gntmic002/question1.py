#Assignment 6.1
#Michael Gant
#20/04/2014

#Program right aligns text entered

length = 0
arrWords = []
sText = ""

print("Enter strings (end with DONE):")

while sText != "DONE": #Receives input, appends to an array and continues until DONE is entered
        if len(sText) > length: #finds the longest word entered
                length = len(sText)
        sText = input("")
        arrWords.append(sText)
        
        
print("\nRight-aligned list:")   

for k in range(0, len(arrWords)-1): #prints each word right aligned according to the longest word
        print(" " * (length-len(arrWords[k])) + arrWords[k])
        
        
    