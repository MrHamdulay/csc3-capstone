#Luke Naude
#2014-04-25
#program to count votes

#create heading
print('Independent Electoral Commission\n','-'*32,'\n','Enter the names of parties (terminated by DONE):',sep='')

#create a vote list
vote_list=[]
#creat an empty list for each party
no_repeats=[]

#get votes
x=input()
while x != 'DONE':
    if x not in vote_list:
        no_repeats.append(x)
    vote_list.append(x)
    x=input()

#sort vote list and name list into alphabetical order
vote_list.sort()
no_repeats.sort()

#a loop to count occurences of each item in no_repeats
print('\nVote counts:')
for i in no_repeats:
    x=(vote_list.count(i))
    print(i,' '*(11-len(i)),'- ',x,sep='')
        
    