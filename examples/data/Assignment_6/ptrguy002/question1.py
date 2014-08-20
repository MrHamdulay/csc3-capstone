#Get strings
print("Enter strings (end with DONE):")
strings = []
inp = input()
while inp != "DONE":
    strings.append(inp)
    inp = input()

#Get longest length
longest = max(map(len, strings)) if len(strings) > 0 else 0

#Output
print("\nRight-aligned list:")
for a in strings:
    print(" "*(longest-len(a)) + a)
    
