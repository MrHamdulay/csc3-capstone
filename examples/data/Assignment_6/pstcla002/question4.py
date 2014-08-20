"""UCT marks histogram programme
Claudia Pastellides
23 April 2014"""

mark=input("Enter a space-separated list of marks:\n")
marks=mark.split(" ")
count50,count60,count70,count75,count80=0,0,0,0,0 # starting values

for i in marks:
    x=eval(i)
    if 0<=x<50: #adding to count for marks in that range
        count50+=1
    elif 50<=x<60:
        count60+=1
    elif 60<=x<70:
        count70+=1
    elif 70<=x<75:
        count75+=1
    elif 75<=x<=100:
        count80+=1
        
print("1 |","X"*count80,sep="") #printing out mark ranking and count for that mark
print("2+|","X"*count75,sep="")
print("2-|","X"*count70,sep="")
print("3 |","X"*count60,sep="")
print("F |","X"*count50,sep="")

