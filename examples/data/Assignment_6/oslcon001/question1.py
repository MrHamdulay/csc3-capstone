# right-alighn a list of strings
# Conor O'Sullivan
# 22/04/2014


# Record strings entered in a list
list_str = []
print("Enter strings (end with DONE):")
enter_str = input("")
while enter_str != "DONE":
       list_str.append(enter_str)
       enter_str = input("")

#find length of longest string
max = 0
for x in list_str:
       size = len(x)
       if size> max:
              max = size
              
#print right-alighned list
print("\nRight-aligned list:")
for x in list_str:
       space = max-len(x)
       print(" "*space + x)
       

       