"""Independent Electoral Commission
Emmanuel Conradie
25 April 2014"""

#create list from input
print ("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")
alist = []
string = input()
while string != 'DONE':
     alist.append(string)
     string = input()
     

print("\nVote counts:")  
count = {}

#count votes
for string in alist:             
     if not string in count:
          count[string] = 1
     else:
          count[string] += 1

#print results   
for string in sorted(count): 
     print ("{0:<10}".format(string),"-",count[string])