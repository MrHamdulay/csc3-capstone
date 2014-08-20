'''Repair'''
count = 0
def pair(name):
    global count
    if name =='' or len(name)==1:
        return ''
    elif name[0]==name[1]:
        return name[0]+pair(name[2:])
    else:
        return pair(name[1:])
name = input('Enter a message:\n')
print('Number of pairs:', len(pair(name)))
    