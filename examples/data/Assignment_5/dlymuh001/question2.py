cost = eval(input("Enter the cost (in cents):\n"))
values = [1, 5, 10, 25, 100]
notes = ["1c", "5c", "10c", "25c", "$1"]
amount_given = 0
while amount_given < cost:
    amount_given += eval(input("Deposit a coin or note (in cents):\n"))
change = amount_given - cost
number_of_notes = 0
size = len(notes)
n = size - 1
if change > 0: print("Your change is:")
while change > 0:
    value = values[n]
    note = notes[n]
    number_of_notes = change // value
    change %= value
    n -= 1
    if number_of_notes == 0: continue
    print (number_of_notes, "x", note)