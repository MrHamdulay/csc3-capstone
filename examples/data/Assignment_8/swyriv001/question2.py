#program that uses a recursive function to count the number of pairs of repeated characters in a string
#Rivoningo Seweya
#08 May 2014
count=0
def pair(state):
    global count
    if len(state)<=1:
        print(count)
    elif state[0]==state[1]:
        count=count+1
        return pair(state[2:])
    else:
        return pair(state[2:])
state=input("Enter a message:\n")
print("Number of pairs: ",end="")
pair(state)