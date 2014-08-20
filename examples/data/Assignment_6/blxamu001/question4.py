""" Program that grades students' marks
Aubrey Baloi
23 April 2014"""


marks = []
fail = []
_3rd = []
lower_2nd = []
upper_2nd = []
_1st = []

marks = input("Enter a space-separated list of marks:\n").split()

for i in marks:
    num = eval(i)
    if num <50:
        fail.append(num)
    elif 50<= num <60:
        _3rd.append(num)
    elif 60<= num <70:
        lower_2nd.append(num)    
    elif 70<= num <75:
        upper_2nd.append(num)
    elif num >= 75:
        _1st.append(num)
        

print('1 |',len(_1st)*'X',sep='')
print('2+|',len(upper_2nd)*'X',sep='')
print('2-|',len(lower_2nd)*'X',sep='')
print('3 |',len(_3rd)*'X',sep='')
print('F |',len(fail)*'X', sep='')
        