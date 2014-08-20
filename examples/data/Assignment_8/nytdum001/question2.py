"""Program to count the number of pairs of repeated characters in a string
Dumisani J Nyathi
09-05-2014"""

def pair_count(string):
    global count
    if len(string) <2:
            return ("Number of pairs: " + str(count))
    else:
        if (ord(string[0])) != ord(string[1]):
            return pair_count(string[1:])#to re-invoke the pair_count
        else:
            count+=1
            return pair_count(string[2:])
            

count=0
string=input("Enter a message:\n")
print(pair_count(string))#invoke recursive function pair_count
    
