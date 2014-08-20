marks = input("Enter a space-separated list of marks:\n").split(" ")
dict = {'first': 0 , 'upper2' : 0, 'lower2' : 0, 'third' : 0, 'fail' : 0}
for i in marks:
    if eval(i) >= 75:
        dict['first'] += 1
    elif eval(i) >= 70:
        dict['upper2'] += 1
    elif eval(i) >= 60:
        dict['lower2'] += 1
    elif eval(i) >= 50:
        dict['third'] += 1
    elif eval(i) < 50:
        dict['fail'] += 1
        
print("1 |", 'X'*dict['first'], sep = "")
print("2+|", 'X'*dict['upper2'], sep = "")
print("2-|", 'X'*dict['lower2'], sep = "")
print("3 |", 'X'*dict['third'], sep = "")
print("F |", 'X'*dict['fail'], sep = "")