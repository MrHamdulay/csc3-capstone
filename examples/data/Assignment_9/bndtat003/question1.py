#Program to get marks from a txt and see if the student needs to see the student advisor
#Matthew Bandama
#BNDTAT003
#12-May-2014



def standard_deviation(l):
	
	n = len(l)
	total = 0
	
	for i in l:
		total += i
		
	average = total/n
	
	dev = 0
	
	for j in l:
		calc = (j-average)**2
		dev += calc
	
	stand_dev = ((dev)/n)**0.5
	return(round(stand_dev,2))


def average(l):
	total = 0
	n = len(l)
	for i in l:
		total += i
		
	average = total/n
	
	return((average))



def process(filename):
 
	my_file = open(filename,'r')
	lines = my_file.readlines()
	my_file.close()
	info = []
	info2 = []
	
	for i in range (len(lines)):
		lines[i] = lines[i][:-1]
	
	for j in lines:
		a = j.split(',')
		info.append(a)
	
	for k in range(len(info)):
		info2.append(eval(info[k][(len(info[k])-1)]))
	return([info2,info])



def main():
	print('Enter the marks filename:')
	filename = input()
	
	info = process(filename)
	ave = average(info[0])
	sd = standard_deviation(info[0])
	bad = ave - sd
	
	print('The average is: {0:.2f}'.format(ave))
	print('The std deviation is: {0:.2f}'.format(sd))
	print('List of students who need to see an advisor:')
	
	for i in info[0]:
		
		if i <= bad and sd != 0 :
			index = info[0].index(i)
			print(info[1][index][0])
			


main()
