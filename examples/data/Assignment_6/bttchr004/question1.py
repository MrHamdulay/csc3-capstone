#program to print right aligned list
#chris betteridge
#21 April 2014

word_list = [] 
word = input("Enter strings (end with DONE):\n")
while word != "DONE":
    word_list.append(word)
    word = input()

if len(word_list) > 0:
    Max = len(word_list[0])
    for i in word_list:
        if len(i) > Max:
            Max = len(i) 

print("\nRight-aligned list:")
for i in word_list:
    if len(i) < Max:
        print(" "*(Max - len(i)),i,sep="")
    else:
        print(i)