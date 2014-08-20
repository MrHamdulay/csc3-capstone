print("Enter strings (end with DONE):")
user_input=[]
index=0
user_input.append(input())
while(user_input[index]!="DONE"):
    user_input.append(input())
    index+=1
user_input.remove("DONE")
print("\nUnique list:")
for index in range(len(user_input)):
    if(user_input.index(user_input[index])==index):
        print(user_input[index])
