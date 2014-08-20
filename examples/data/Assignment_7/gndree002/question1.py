def uniq(inlist): 
    # order preserving
    uniques = []
    for item in inlist:
        if item not in uniques:
            uniques.append(item)
    return uniques

x=['']
print("Enter strings (end with DONE):")
while x[-1]!="DONE":
    x.append(input())
print("\nUnique list:")
x=uniq(x)
x.remove('')
x.remove('DONE')
for i in x:
    print(i)