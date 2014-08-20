#b.booi
#23 April 2014
#Align

def align():
     print("Enter strings (end with DONE):")
     i = 0
     namelist = []
     while i != -1:
          namelist.append(input(""))
          if namelist[i] == "DONE":
               i = -1
          else:
               i+=1
     print()
     
     print("Right-aligned list:")
     
     listlen = len(namelist)-1
     
     longestWord = max(len(s) for s in namelist)
     #print(longestWord)
     StringNum = str(longestWord)
     newString = "{0:>"+StringNum+"}"
     
     for x in range(listlen):
          print(newString.format(namelist[x]))
     

     #print(list[0:i])
               

align()
     
    