"""Function to check for pairs
James Cushway
10-052014"""
place=0
count=0
word=input("Enter a message:\n")
def paircount(place,count):
    if place<len(word)-1:
        if word[place]==word[place+1]:
            count+=1
            place+=2
            paircount(place,count)
               
        else:
            place+=1
            paircount(place,count)
        
    elif place==len(word) and len(word)%2==0:
        print('Number of pairs:',count)
    else:
        print('Number of pairs:',count)
        
    
paircount(place,count)

        
        