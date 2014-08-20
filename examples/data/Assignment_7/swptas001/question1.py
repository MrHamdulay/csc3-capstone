### Tashiv Sewpersad (SWPTAS001)
### Assignment 7 - Question 1
### 01-05-2014

## Live code
aWords = []
# Input
sInput = input("Enter strings (end with DONE):\n")
while sInput.upper() != "DONE":
  if not (sInput in aWords): # Checks if its a new word 
    aWords.append(sInput)
  sInput = input()
 # Output
print()
print("Unique list:")
for i in aWords:
  print(i)