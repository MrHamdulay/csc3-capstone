'''program to print out list of strings righ-aligned
sankara mallane
19 april 2014'''

Str = []

xStr = input("Enter strings (end with DONE):\n")


while xStr != 'DONE':
    Str.append (xStr)
    xStr = input("")    
    
longest_word = 0

for xStr in (Str):
    if len(xStr)> longest_word:
        longest_word = len(xStr)
print()
print ("Right-aligned list:")

for xStr in (Str):
    print(xStr.rjust(longest_word))