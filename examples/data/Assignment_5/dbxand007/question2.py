"""Cherise Dube
12 April 2014
Program to determine the change given from a vending machine"""

#asks for cost and deposit until the deposit is equal to or exceeds the cost

cost=eval(input("Enter the cost (in cents):\n"))
if cost>0:
    #Function ensures that the correct deposit is given and returns the amount put in machine
 def correct_deposit():
     deposit=eval(input("Deposit a coin or note (in cents):\n"))
     while deposit<cost:
         deposit1=eval(input("Deposit a coin or note (in cents):\n"))
         deposit+=deposit1
     return deposit
 
 change=correct_deposit()-cost
 if change>0:
     print("Your change is:")
 else:
     pass
 
 #Determines how many $1 notes should be given (prints and returns value of change less money $1 notes)
 def calc_change(change):
     count=0
     if change>=100:
             while change>=100:
                         change-=100
                         count+=1
             print(count,"x $1")    
             return change
     else:
         return change
 #Determines how many 25c should be given
 change=calc_change(change)
 def calc_change1(change):
     count1=0
     if 25<=change<100:
         while 25<=change<100:
             change-=25
             count1+=1            
                             
         print(count1,"x 25c")
         return change
     else:
         return change
 
 #Determines how many 10c should be given   
 change=calc_change1(change)
 def calc_change2(change):
     count2=0
     if 10<=change<25:
         while 10<=change<25:
             change-=10
             count2+=1
         print(count2,"x 10c")
         return change
     
     else:
         return change
 #Determines how many 5c should be given
 change=calc_change2(change)
 def calc_change3(change):
     count3=0
     if 5<=change<10:
         while 5<=change<10:
                 change-=5
                 count3+=1
         print(count3,"x 5c")
         return change
     else:
         return change
                         
 #Determines how many 1c should be given
 change=calc_change3(change)
 if 1<=change<5:
     count4=0
     while 1<=change<5:
             change-=1
             count4+=1
     print(count4,"x 1c")
                             
 else: pass
                 
else:
 pass
 
 
                 
                     
            
 
    