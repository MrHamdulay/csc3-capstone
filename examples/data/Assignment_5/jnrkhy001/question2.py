#Khyati Jinerdeb
#JNRKHY001
#Assignment 5
#program to calculate change based on the amount paid
#Date:17/04/2014


def main():
   cost=eval(input("Enter the cost (in cents):\n"))
   if cost>0:
      deposit=eval(input("Deposit a coin or note (in cents):\n"))
      x=0
      while deposit<cost: #use of while loop while a condition is true
         x=eval(input("Deposit a coin or note (in cents):\n"))
         deposit=deposit+x
      
      change=deposit-cost
      coin=0
      if change>0:
         print("Your change is:")
         
         if change>=100:
            coin=change//100 #to get the number of a particular coin returned
            change=change%(coin*100)
            print(coin,"x","$1")
            
         if change>=25:
            coin=change//25
            change=change%(coin*25)
            print(coin,"x","25c")
            
         if change>=10:
            coin=change//10
            change=change%(coin*10)
            print(coin,"x","10c")
            
         if change>=2:
            coin=change//2
            change=change%(coin*2)
            print(coin,"x","2c")
            
         if change>=1:
            coin=change//1
            change=change%(coin*10)
            print(coin,"x","1c")
            
      else:
         print()
            
main()            
            
            
            
            
            
            
            
            
        





    

    
    
    
    
