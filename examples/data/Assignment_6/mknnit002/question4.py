#mknnit002
#question 4 ass 6

marks=input("Enter a space-separated list of marks:\n")
marklist=marks.split(" ")
category=["1 ","2+","2-","3 ","F "]
countlist=[0,0,0,0,0]
for k in marklist:
      if eval(k)<50:
            countlist[4]+=1
      if eval(k)<60 and eval(k)>=50:
            countlist[3]+=1
      if eval(k)<70 and eval(k)>=60:
            countlist[2]+=1            
      if eval(k)<75 and eval(k)>=70:
            countlist[1]+=1            
      if eval(k)<=100 and eval(k)>=75:
            countlist[0]+=1
          
for i in range(5):
      print(category[i],"|","X"*countlist[i],sep="")