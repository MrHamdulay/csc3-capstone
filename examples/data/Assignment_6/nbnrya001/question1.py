
names = []

print('Enter strings (end with DONE):')

x = input()
maxlet = 0

while x != 'DONE':
    names.append(x)
    x = input()


print()
print('Right-aligned list:')

f = lambda x : max(maxlet, len(x))

for i in names:
    maxlet = f(i)

g = lambda x : '{0:>{1}}'.format(x, maxlet)

for i in names:
    print(g(i))
