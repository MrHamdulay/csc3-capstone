# histogram output of marks
# Danielle Sher

from collections import Counter

marks = input("Enter a space-separated list of marks:\n")
marklist = marks.split()

symbol_list = []
for i in marklist:
    if int(i) < 50:
        symbol_list.append('F')
    elif 50 <= int(i) < 60:
        symbol_list.append('3')
    elif 60 <= int(i) < 70:
        symbol_list.append('2-')
    elif 70 <= int(i) < 75:
        symbol_list.append('2+')
    elif 75 <= int(i) <= 100:
        symbol_list.append('1')
    
    
counts = Counter(symbol_list)

keys = counts.keys()
values = counts.values()

if '1' in counts == False:
    print ("1" + " " + "|")
else:
    print("1" + " " + "|" + "X"*counts['1'])

if '2+' in counts == False:
    print("2+" + "|")
else:
    print("2+" + "|" + "X"*counts['2+'])

if '2-' in counts == False:
    print("2-" + "|")
else:
    print("2-" + "|" + "X"*counts['2-'])
if '3' in counts == False:
    print("3" + " " + "|")
else:
    print("3" + " " + "|" + "X"*counts['3'])
if 'F' in counts == False:
    print("F" + " " + "|")
else:
    print("F" + " " + "|" + "X"*counts['F'])

          
          
