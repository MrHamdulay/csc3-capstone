#A programme to count the number of reapeted characters on a string
#lebogang masila
# 09 May 2014


message=input("Enter a message:\n")
def count(message):
    if len(message)<=1:
        return 0
    if message[0]==message[1]:
        return 1+ count(message[2:])
    else:
        return count(message[1:])
print("Number of pairs:",count(message))
