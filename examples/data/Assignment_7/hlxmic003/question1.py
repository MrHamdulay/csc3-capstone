# Michaela Heale
# Assignment 7 Question 1

sentence = []
opt = input("Enter strings (end with DONE):\n")
while not opt == "DONE":
    if not opt in sentence:
        sentence.append(opt)
    opt = input()

print("\nUnique list:")
for disc in sentence:
    print(disc)
    
