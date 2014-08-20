# count number of votes
# Conor O'Sullivan
# 22/04/2014


print("Independent Electoral Commission\n--------------------------------")

#obtaining votes
print("Enter the names of parties (terminated by DONE):")
party = []
votes = {}
enter = input("")
while enter != "DONE":
       if party.count(enter) == 0:
              party.append(enter)
       try: 
              votes[enter] += 1
       except: 
              votes[enter] = 1
       enter = input("")
party.sort()

# printing votes
print("\nVote counts:")
for x in party:
       x_for = "{0:<10} -".format(x)
       print(x_for,  votes[x])

       


