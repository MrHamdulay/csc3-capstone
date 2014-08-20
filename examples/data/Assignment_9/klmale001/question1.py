"""Question 1
13 May 2014
Alexi Kalamoudacos"""

import math
y={}
x=[]
f=input('Enter the marks filename:\n')
f = open(f, 'r')
g = f.readlines()
f.close()
z=[]
  
#edits the character in the new line
for i in range (len (g)-1):
    g[i] = g[i][:-1]
  
#removes extra quotes
for i in range (len (g)):
    if g[i] != "":
        if g[i][0]== '"' or g[i][0]== "'":
            g[i] = g[i][1:]
            if g[i][-1] == '"' or g[-1]== "'":
                g[i] = g[i][:-1]
#extract the results
for i in range (len (g)):
    e = g[i].split (',')
    y[e[0]]=eval(e[1])
    z.append(e[0])
for key in y:
    x.append(y[key])
  
a = 0
b = 0
for i in x:
    a = a + i
a = a/len(x) #calculates the mean average  
  
for i in x:
    b = b + (i - a)**2
  
b = math.sqrt(b/len(x)) #works out std deviation  
See = a - b
a ="{:.2f}".format(a)
b ="{:.2f}".format(b)
print('The average is:' , a)
print('The std deviation is:', b)
  
  
d=False
for i in y.keys():
    if y[i] < See:
        d=True
if d: #prints out if required
    print('List of students who need to see an advisor:')
    for i in z:
        if y[i] < See:
            print(i)