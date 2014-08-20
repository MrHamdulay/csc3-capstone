"""Program to calculate change and simulate vending machine
Author: Pankaj Munbodh
16 April 2014"""

#create loop to check whether amount of money given is greater than cost
cost=eval(input("Enter the cost (in cents):\n"))
exceed_cost =0
if cost==0: # to cater for exception of cost being equal to zero. This prevents rest of program from being executed.
                  pass
else:
                  while exceed_cost < cost:
                                    money = eval(input("Deposit a coin or note (in cents):\n"))
                                    exceed_cost+=money
                                    if exceed_cost==cost:break
                  else:print("Your change is:")

#process change by creating list.
                  change1 = exceed_cost - cost
                  liste=[100,25,10,5,1]

#Divide change by each item in list to get remainder and do further division if necessary.
#Also store answers to integer division and finally output change in terms of coins and notes available.
                  for i in range(len(liste)):
                                    x=change1//liste[i]
                                    change1=change1%liste[i]
                                    if x==0:
                                                      continue
                                    elif i==0:
                                                      print(x,'x','$1')
                                    elif i==1:
                                                      print(x,'x','25c')
                                    elif i==2:
                                                      print(x,'x','10c')
                                    elif i==3:
                                                      print(x,'x','5c')
                                    elif i==4:
                                                      print(x,'x','1c')
                  
                                                                          
                                    
                     
