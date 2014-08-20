"""A5Q2 - Coin change
Keegan Crankshaw
14/4/2014"""

CoinsIn = 0
coins_avail = [100, 25, 10, 5, 1]

def main():   
   global CoinsIn
   cost = eval(input("Enter the cost (in cents):\n"))
   while cost > CoinsIn:       
      toadd= eval(input("Deposit a coin or note (in cents):\n"))
      CoinsIn += toadd
   
   if cost < CoinsIn:
      amount = CoinsIn-cost
      print("Your change is:")
      CalcChange(amount)    

def CalcChange(amount):
   for i in coins_avail:
      if amount == 0:
         break      
      coincount = amount//i
      if (coincount >= 1) and (i==100):
         if coincount != 0:
            print(coincount, "x $1")
         amount = amount - coincount*i
         if amount == 0:
            break
      else:
         if coincount != 0:
            print(coincount, " x ", i, "c", sep="")
         amount-= coincount*i   
         
    
if __name__ == "__main__":
   main()