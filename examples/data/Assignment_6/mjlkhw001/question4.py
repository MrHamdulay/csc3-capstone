# Histogram representation
# Khwezi Majola
# MJLKHW001
# 20 April 2014

def histo():
    marks = input('Enter a space-separated list of marks:\n') #Input for the marks
    listm = marks.split(' ') #List of marks
    histo = [['1', ''],['2+', ''],['2-',''],['3',''],['F','']] #List for the histogram
    for i in range(len(listm)):
        if eval(listm[i]) >= 75:
            histo[0][1] += 'X'
        elif eval(listm[i]) >= 70:
            histo[1][1] += 'X'        
        elif eval(listm[i]) >= 60:
            histo[2][1] += 'X'
        elif eval(listm[i]) >= 50:
            histo[3][1] += 'X'   
        else:    
            histo[4][1] += 'X'
    for j in range(5):
        output = '{0:<2}|{1}'.format(histo[j][0], histo[j][1])
        print(output)
histo()