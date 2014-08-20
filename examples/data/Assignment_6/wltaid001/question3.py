"""Aiden Walton
WLTAID001
Question 3 - Assignment 6"""
parties={}
print("Independent Electoral Commission")
print("--------------------------------")
raw_input=input("Enter the names of parties (terminated by DONE):\n")
while raw_input!="DONE":
    if raw_input!="DONE":
        if not raw_input in parties:
            parties[raw_input]=1
        else:
            parties[raw_input]+=1
        raw_input=input("")
alph=sorted(parties.keys())
print()
print("Vote counts:")
for word in alph:
    print(word,end="")
    print(" "*(11-len(word)),end="")
    print("-", parties[word],end="")
    print()