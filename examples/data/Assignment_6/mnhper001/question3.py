#Author:Percival Munhuwaani
#Program: A program to count the number of votes for each political party in an election
#Date:24/04/2014

def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    party_name=input("Enter the names of parties (terminated by DONE):\n")
    name_list={} #creating a dictionary to store the party names and their votes
    key_list=[] #cerating a list to store the party names as keys
    while party_name!="DONE":#getting the loop started
        if party_name not in name_list.keys():
            name_list[party_name]=1
            key_list.append(party_name)
        else:
            name_list[party_name]=name_list[party_name]+1 #counting the votes for each party name
        party_name=input()
    key_list.sort() #putting the party names in alphabetical order
    print("\nVote counts:")
    for key in key_list:
        print(key,(10-len(key)+1)*" ","-"," ",(name_list[key]),sep="")
main()