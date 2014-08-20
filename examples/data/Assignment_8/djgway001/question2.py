#determining number of pairs in string
#wayne de jager
#6 may 2014

n=0 #starting tally
def pairs(x):
    if len(x)==1 or len(x)==0:
        return 0 #cannot be pairs if num of characters is less than 2
    elif x[0]==x[1]: #check to see matching adjacent characters
        return pairs(x[2:])+1 # if pair, add 1 to tally
    else:
        return pairs(x[1:]) #continue but dont add to tally
x=input("Enter a message:\n")
print("Number of pairs:",pairs(x))