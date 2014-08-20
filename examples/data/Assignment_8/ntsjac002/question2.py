'''A program that counts number of pairs of repeated characters in a string
Jacob Ntesang
06 May 2014'''

#Get the message from the user
S = input("Enter a message:\n")
def Pairs(S):
    if len(S) < 2 or S == "":
        return 0
    else:
        if S[0] == S[1]:
            return (1 + Pairs(S[2:]))
        else:
            return Pairs(S[1:])
      
print("Number of pairs:",Pairs(S))