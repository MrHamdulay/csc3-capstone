#ComSci Assignment 6
#Nikhil Jiten Naik
#25/04/2014
#Question 3

votes={}
group=input("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")
while group!="DONE":
  
    if group in votes.keys():
        votes[group]+=1
    else:
        votes[group]=1
    group=input('')
print()
print("Vote counts:")
for key in sorted(list(votes.keys())):
    print(key.ljust(10),"-",votes[key])

marks=input("Enter a space-separated list of marks:\n")

mark=marks.split(" ")

fail=0
third=0
lowersecond=0
uppersecond=0
first=0

for i in mark:
    if 0 <= eval(i) < 50:
        fail+=1
    elif 50 <= eval(i) < 60:
        third+=1
    elif 60 <= eval(i) < 70:
        lowersecond+=1
    elif 70 <= eval(i) < 75:
        uppersecond+=1
    elif 75 <= eval(i) <= 100:
        first+=1

print("1 |"+"X"*first)
print("2+|"+"X"*uppersecond)
print("2-|"+"X"*lowersecond)
print("3 |"+"X"*third)
print("F |"+"X"*fail)