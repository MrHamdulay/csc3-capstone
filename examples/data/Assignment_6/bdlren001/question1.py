# a Python program where the user can enter a list of strings followed by the sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string
# Budeli Rendani
# BDLREN001
# 20/04/2014

names=[] # Indroducing an empty list of names
def main():
    global names # Bringing in the empty list inside the function
    x=input("Enter strings (end with DONE):\n") # Obtaining the strings from user
    while x !="DONE":
        names.append(x) # Adding the names to the empty list
        x=input() 
    print("\nRight-aligned list:")
    for i in names:
        n=max(names, key=len) #Finding the longest string in the list
        q=len(n) # Finding the lenght of the longest string
        p=len(i) # Finding the the length of the individual string in the list
        z=q-p # Calculating the spacing for the alignment
        print(z*" "+i)
    return
main()