x = input('Enter a space-separated list of marks:\n')
LIST = x.split(" ")

FAIL = []
RD_3 = []
LOWER_ND_2 = []
UPPER_ND_2 = []
ST_1 = []
for i in LIST:
    if eval(i) < 50:
        FAIL.append(i)
    if 50 <= eval(i) < 60:
        RD_3.append(i)
    if 60 <= eval(i) < 70:
        LOWER_ND_2.append(i)
    if 70 <= eval(i) <75:
        UPPER_ND_2.append(i)
    if eval(i) >= 75:
        ST_1.append(i)
print('1 |','X'*len(ST_1),sep='')
print('2+|','X'*len(UPPER_ND_2),sep='')
print('2-|','X'*len(LOWER_ND_2),sep='')
print('3 |','X'*len(RD_3),sep='')
print('F |','X'*len(FAIL),sep='')
