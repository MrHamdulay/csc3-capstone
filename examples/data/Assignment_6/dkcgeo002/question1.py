__author__ = 'George de Kock'
""" Printing Strings
    2014-4-20   """

names = []
length = 0
print("Enter strings (end with DONE):\n")
while True:
    nextstr = input("")
    if nextstr == "DONE":
        break
    names.append(nextstr)
    if len(nextstr) > length:
        length = len(nextstr)


length = str(length)
print("Right-aligned list:")
for x in names:
    a = "{0:>{1}}".format(x,length)
    print(a)