# Lehlogonolo Masetla
# 21 April 2014.

marks = input("Enter a space-separated list of marks:\n")

x = marks.split(" ")

x.sort() # sorts the list in ascending order

x.reverse() # reverse the list into discending order

# lists according to category
fail = []
third = []
lower_second = []
upper_second = []
first = []

#loop to add marks into relevant list class
for i in range(len(x)):
   if int(x[i]) >= 75:
      first.append(x[i])
   elif 70 <= int(x[i]) < 75:
      upper_second.append(x[i])
   elif 60 <= int(x[i]) < 70:
      lower_second.append(x[i])
   elif 50 <= int(x[i]) < 60:
      third.append(x[i])
   else:
      fail.append(x[i])
      
print("1"," ","|","X"*len(first),sep="")
print("2+","|","X"*len(upper_second),sep="")
print("2-","|","X"*len(lower_second),sep="")
print("3"," ","|","X"*len(third),sep="")
print("F"," ","|","X"*len(fail),sep="")
