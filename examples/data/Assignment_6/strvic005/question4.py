"""program to create histogram from list of marks
vicky stark
23 april 2014"""

z=input("Enter a space-separated list of marks:\n")

list_of_values=z.split(' ')

#define classes for marks
fail=0
third=0
lower_second=0
upper_second=0
first=0

#loop through list and classify mark
for i in list_of_values:
     value=eval(i)
     if value<50:
          fail+=1
     elif 50<=value<60:
          third+=1
     elif 60<=value<70:
          lower_second+=1
     elif 70<=value<75:
          upper_second+=1
     else:
          first+=1
          

#create axis
for y in range(0,5):
     for x in range(0,5):
          if x==0 and y==0:
               print("1 ", end='')
          elif x==0 and y==1:
               print("\n2+", end='')
          elif x==0 and y==2:
               print("\n2-", end='')
          elif x==0 and y==3:
               print("\n3 ", end='')
          elif x==0 and y==4:
               print("\nF ", end='')
          elif x==1:
               print("|",end='')
          
          #to plot values    
     if y==4 :
          print('X'*fail, end='')
     elif y==3:
          print('X'*third, end='')
     elif y==2 :
          print('X'*lower_second, end='')
     elif y==1 :
          print('X'*upper_second, end='')
     elif y==0:
          print('X'*first, end='')        