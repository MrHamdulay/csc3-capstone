"""A programme to count the number of reapeted characters on a string
Sthabiso Andile Gazu
May 2014"""

#ask the user for a message
message=input("Enter a message:\n")
def count(message):
    if len(message)<=1:
        return 0
    if message[0]==message[1]:
        return 1+ count(message[2:])
    else:
        return count(message[1:])
print("Number of pairs:",count(message))
