# James Behr
# 2014-04-23
# Assignment 6 Question 3

parties = {} # dictionary to hold names
print('Independent Electoral Commission')
print('--------------------------------')
print('Enter the names of parties (terminated by DONE):')
# Loop until sentinel is reached
while True:
    s = input()
    if s == 'DONE':
        break
    if s in parties.keys():
        parties[s] += 1
    else:
        parties[s] = 1
        
print() # Blank line
print('Vote counts:')
# Output by looping through sorted keys
for key in sorted(parties):
    print('{:10} - {}'.format(key, parties[key]))
    