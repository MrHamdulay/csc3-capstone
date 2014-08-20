x=eval(input("Enter a year:\n"))
a=x/4
b=x//4
c=x/400
d=x//400
e=x/100
f=x//100
g="is a leap year."
h="is not a leap year."
if c==d:
    print(x,g)
elif a==b:
    if e!=f:
        print(x,g)
    else:
        print(x,h)
else:
    print(x,h)