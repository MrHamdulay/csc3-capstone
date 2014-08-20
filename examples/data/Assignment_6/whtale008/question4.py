""" mark catagorising programm
ALexander Whiting
14 April 2014 """


cat = {'1':0,'2+':0,'2-':0,'3':0,'F':0} # creating dictionary of catagories

print("Enter a space-separated list of marks:")
marks = input("").split(" ")

for mark in marks:
    i = eval(mark)
    if i < 50:
        cat['F'] += 1
        
    elif  50 <= i < 60:
        cat['3'] += 1
    elif 60 <= i < 70:
        cat['2-'] +=1
    elif 70 <= i < 75:
        cat['2+'] += 1
    elif i >= 75:
        cat['1'] += 1
        
cats = ['1','2+','2-','3','F'] #because position of key in list is not permanent
for j in cats:
    print(j+" "*(2-len(j))+"|"+"X"*cat[j])