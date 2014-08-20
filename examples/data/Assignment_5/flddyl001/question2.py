v_amount = eval(input("Enter the cost (in cents):\n"))

v_sum = 0

while v_sum < v_amount:
    
    v_deposit = eval(input("Deposit a coin or note (in cents):\n"))
    
    v_sum += v_deposit
    
v_remainder = v_sum - v_amount
    
v_dollars = v_remainder//100

v_remainder = v_remainder - v_dollars*100

v_quarters = v_remainder//25

v_remainder = v_remainder - v_quarters*25

v_tens = v_remainder//10

v_remainder = v_remainder - v_tens*10

v_ones = v_remainder

if v_sum != v_amount:
    print("Your change is:")

if v_dollars != 0:
    print(v_dollars,"x $1")
if v_quarters != 0:
    print(v_quarters,"x 25c")
if v_tens != 0:
    print(v_tens, "x 10c")
if v_ones !=0:
    print(v_remainder, "x 1c")