coins = [1,25,10,5,1]
x = eval(input('Enter a cost (in cents):\n'))
y=0
while y<x:
    z = eval(input("Deposite a coin or a note (in cents):\n"))
    y = y + z
change = y - x
print('Your change is:')
a = change / coins
if a%coins!=0:
    break
else:
    print(a, 'x', coins)