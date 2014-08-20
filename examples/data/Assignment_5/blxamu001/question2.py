"""Program that simulates a vending machine

Name: Aubrey Baloi

Student number: BLXAMU001

Date: 17-April-2014"""

def get_money():
	''' Function that asks for a number and returns it'''
	
	cash = eval(input('Deposit a coin or note (in cents):\n'))
	return (cash)

def get_change(last_amount,cost):
	
	'''Get the change in $1,25c,10c,5c,1c'''
	
	change_in_cents = last_amount - cost
	
	if change_in_cents == 0:
		
		a = 1
	
	
	
	else:
		
		dollar_coins = change_in_cents//100 # find out how many $1 notes/coins are needed
		
		dollar_remainder = change_in_cents%100 # find out the remainder so i can use it later with other notes/coins
		
		#process is repeated for 25c,10c,5c,1c,
		
		twenty_five_coins = dollar_remainder//25
		
		twenty_five_remainder = dollar_remainder%25
		
		ten_coins = twenty_five_remainder//10
		
		ten_remainder = twenty_five_remainder%10
		
		five_coins = ten_remainder//5
		
		five_remainder = ten_remainder%5
		
		one_coins = five_remainder
		
		print('Your change is:')
		
		for run in [dollar_coins, twenty_five_coins, ten_coins, five_coins, one_coins]:
			# run through all the amounts of coins printig respective amounts
			
			if run == 0: # if amount is zero then it skips that particular amount
				
				continue
			
			elif run == dollar_coins:
				
				print(dollar_coins,'x $1')
				
				dollar_coins = 0
				
			elif run == twenty_five_coins:
				
				print(twenty_five_coins,'x 25c')
				
				twenty_five_coins = 0
				
			elif run == ten_coins:
				
				print(ten_coins,'x 10c')
				
				ten_coins = 0
				
			elif run == five_coins:
				
				print(five_coins,'x 5c')
				
				five_coins = 0
				
				
			elif run == one_coins:
				
				print(one_coins,'x 1c')
				
				one_coins = 0

def main():
	''' main function - get amounts, - more input until cost is exceeded by money
	and. Calls on the get_change function for change'''
	
	cost = eval(input('Enter the cost (in cents):\n'))
	
	if cost > 0:
		initial_amount = get_money()
	
	
		total_amount = initial_amount
	
		while total_amount < cost:
		
			more = get_money()
		
			total_amount = total_amount + more
		
		get_change(total_amount,cost)

if __name__ == '__main__':

	main()
