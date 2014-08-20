from functools import reduce
import math
inp = input("Enter a function f(x):\n")
f = lambda x: eval(inp)
print(reduce(lambda l,k: l+"\n"+k, map(lambda y: reduce(lambda a,b: a+b, map(lambda x: "o" if round(f(x))==y else "+" if (x == 0 and y == 0) else "|" if (x == 0) else "-" if (y == 0) else " ", range(-10, 11))), list(range(-10, 11))[::-1])))
