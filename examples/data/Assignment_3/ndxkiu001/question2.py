#question 2

h = eval(input("Enter the height of the triangle:\n"))
start = h*2-1

s=""

for x in range(h):
    ts=" "*x
    ts = ts+"*"*start
    ts = ts+(" "*x)
    s = ts +"\n"+ s
    start = start -2

print (s)
