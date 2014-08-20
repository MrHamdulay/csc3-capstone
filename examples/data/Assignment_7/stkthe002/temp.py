
a = [[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]]
b = [1,1]
c = 1
print(a)
a.insert(0,b)
print(a)
a.insert(5,b)
print(a)
a = a
for vec in a:
    vec.insert(0,c)
    vec.insert(2,c)
    print(a)
print(a)