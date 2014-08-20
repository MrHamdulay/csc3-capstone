texts = []
text= input("Enter strings (end with DONE):\n")
while text != 'DONE':
    texts.append(text)
    text = input("")
    
print("\n""Unique list:") 

dic = {}
for i, sen in enumerate(texts):
    for word in sen.split():
        if word not in dic:         # you just need these
            dic[word] = set()       # two extra lines
            dic[word].add(i)
            print(word)

