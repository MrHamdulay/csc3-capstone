'''program to count the number of votes in an election
Name: MICEALA NAIDOO
Student Number: NDXMIC014
Date: 22-April-2014'''

import question1

def countvotes(my_list):
	
	votes = {}
	
	count = 1
	for i in my_list:
		
		if i not in votes:
		
			votes[i] = count
		
		else:
			votes[i] = votes[i] + 1
	
	return(votes)



def getcandidates(names):
	
	candidates = []
	
	for i in names:
		
		if i not in candidates:
			
			candidates.append(i)
	
	candidates.sort()
	
	return(candidates)




def print_results(names,votes):
	length = 11
	
	
	for i in names:
		
		space = length - len(i)
		
		print(i,' '*space,'- ',votes[i],sep = '')




def main():
	
	print('Independent Electoral Commission\n--------------------------------')
	print('Enter the names of parties (terminated by DONE):')
	
	all_names = question1.get_list()
	
	candidates = getcandidates(all_names[0])
	
	votes = countvotes(all_names[0])
	
	print()
	
	print('Vote counts:')
	print_results(candidates,votes)




if __name__=='__main__':
	
	main()




