# Student Number: PRTNIC017
# Date: 4/13/14

deposit = 0

cost = eval(input('Enter the cost (in cents):\n'))

while deposit < cost:
    deposit += eval(input('Deposit a coin or note (in cents):\n'))

unsorted_change = deposit - cost
change_names = ['$1', '25c', '10c', '5c', '1c']
change_values = [100, 25, 10, 5, 1]
sorted_change = [0, 0, 0, 0, 0]

if unsorted_change != 0:
	print('Your change is:')

for index in range(0, 5, 1):
    while unsorted_change >= change_values[index]:
        unsorted_change -= change_values[index]
        sorted_change[index] += 1
    if sorted_change[index] != 0:
        print(sorted_change[index], 'x', change_names[index])


