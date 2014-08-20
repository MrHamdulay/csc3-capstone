"""a programme to count the no. of votes
Sthabiso Andile Gazu
April 2014"""
#welcom note
x="""Independent Electoral Commission
--------------------------------"""
print(x)
 #ask for voting , parties names
List_of_parties=[]
parties=input("Enter the names of parties (terminated by DONE):\n")
while parties!="DONE":
    List_of_parties.append(parties)
    parties=input("")    
counter={}
#to return
print()
print("Vote counts:")
k=len('Vote counts')
for parties in List_of_parties:
    if not parties in counter:
        counter[parties]=1
    else:
        counter[parties]+=1        
for parties in sorted(set(counter)):
    print(parties," "*(k-len(parties)),"-",' ',counter[parties], sep="")