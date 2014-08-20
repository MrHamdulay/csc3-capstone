x = input("Enter a space-separated list of marks:\n")
b = x.split()
y = []

fail = 0
third = 0
sec_low = 0
sec_up = 0
first = 0 

for j in range (len(b)):
    b[j] = eval(b[j])
    y.append(b[j])
    
for mark in b:
    if ( 0 <= mark < 50):
        fail += 1
    elif (mark < 60):
        third += 1
    elif (mark < 70):
        sec_low += 1
    elif (mark < 75):
        sec_up += 1
    else:
        first += 1
        
print("1 |","X"*first,sep='')
print("2+|","X"*sec_up,sep='')
print("2-|","X"*sec_low,sep='')
print("3 |","X"*third,sep='')
print("F |","X"*fail,sep='')
        