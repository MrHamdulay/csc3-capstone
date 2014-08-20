#GLMSUM001
#Sumayah Goolam Rassool
#10 May 2014

sent = input("Enter a message:\n")

def counting(sent):
    
    if len(sent)<2:
        return 0
    elif sent[0]==sent[1]:
        return 1 + counting(sent[2:])
    else:
        return counting(sent[1:])
print("Number of pairs:",counting(sent))