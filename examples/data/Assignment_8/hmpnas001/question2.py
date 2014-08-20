"""program to count pairs
nasonkwe hampwaye
2014-05-08"""
message=input("Enter a message:\n")
count=0
def friendlyletter(message):
#base case
    if len(message)<=1:
        return 0
#recursive step
    else:
        if message[0]==message[1]:
            return (count + 1) + friendlyletter(message[2:])
        else:
            return count + friendlyletter(message[1:])      
    
print("Number of pairs:",friendlyletter(message))    
friendlyletter(message)        