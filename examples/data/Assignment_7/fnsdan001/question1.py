wrd = input("Enter strings (end with DONE):\n")
if wrd == "DONE":
    print()
    print("Unique list:")
else:
    
    results = []
    results.append(wrd)
    while wrd!= "DONE":
        wrd = input()
        if wrd not in results and wrd != "DONE":
            results.append(wrd)
    print()
    print("Unique list:")
    
    print(("\n").join(results))
        
    
    
    
    
