#Program that counts the number of pairs of repeated letters
#Gordon Skhosana
#8/05/2014
count=0
def repeated(string):
    global count
    if len(string)==1:
        return ""
    elif len(string)==0:
        return ""    
    elif string[0]!=string[1]:
        repeated(string[1:])
    else: 
        count+=1
        repeated(string[2:])
    return count
def main():
    string=input("Enter a message:\n")
    print("Number of pairs:",repeated(string))
main()