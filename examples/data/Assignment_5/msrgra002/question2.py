#Grant Meeser
#MSRGRA002
#15/04/2014

def change(cents):
	dollars = cents//100
	cents = cents%100
	cents25 = cents//25
	cents = cents%25
	cents10 = cents//10
	cents = cents%10
	cents5 = cents//5
	cents = cents%5
	cents2 = cents//2
	cents = cents%2
	cents1 = cents//1

	output=''
	if dollars>0 : output+= '\n'+str(dollars)+' x $1'
	if cents25>0 : output+= '\n'+str(cents25)+' x 25c'
	if cents10>0 : output+= '\n'+str(cents10)+' x 10c'
	if cents5>0 : output+= '\n'+str(cents5)+' x 5c'
	if cents2>0 : output+= '\n'+str(cents2)+' x 2c'
	if cents1>0 : output+= '\n'+str(cents1)+' x 1c'

	if output!='' :print('Your change is:',output)

cost = int(input('Enter the cost (in cents):\n'))
deposit = 0

while deposit<cost:
	deposit+=int(input('Deposit a coin or note (in cents):\n'))

change(deposit-cost)
