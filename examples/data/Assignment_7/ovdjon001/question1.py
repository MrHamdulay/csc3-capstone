"""Assignment 7, question 1 , question1.py
by Jonathan Ovadia 
1 May 2014"""
def main():
    list1 = []
    list1 = inputList()
    print("\nUnique list:")
    for i in uniqueList(list1):
        print(i)
def uniqueList(l):
    list1 = []
    for i in l:
        if i not in list1:
            list1.append(i)
    return list1
def inputList():
    list1 = []
    print("Enter strings (end with DONE):")
    line = input("")
    while line!="DONE":
        list1.append(line)
        line = input("")
    return list1
if __name__ == "__main__": main()