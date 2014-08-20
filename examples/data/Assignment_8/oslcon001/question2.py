# Counts the number of repeated charaters in a string
# Conor O'Sullivan
# 04/05/2014


# Get input
sent = input("Enter a message:\n")

# Recursive function
def pairs(sent):
       
       if sent == "" or len(sent) == 1:
              return 0
       elif sent[0] != sent[1]:
              return pairs(sent[1:])
       elif sent[0] == sent[1]:
  
              try:
                     
                     return 1+ pairs(sent[2:])
              except: 
                     return 1 + pairs("")
       
print("Number of pairs:", pairs(sent))
       