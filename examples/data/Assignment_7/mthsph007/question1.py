""" Sphiwe Muthembi - 27/04/2014
    MTHSPH007
    Question 1 - Assignment 7 """


#======================================#
 # Comments:
 #=========
 #this program must take in a series of inputs
 #terminate with DONE. (USE A WHILE FUNCTION)
 #before printing check if list has duplicates and remove them. (Might need two lists )
#======================================#

#input:

words = input ('Enter strings (end with DONE):\n')

#lists:
arlistinput = []
arlistfiltered = {}
array2 = []
#While function:

arlistinput.append(words)

while words != 'DONE':
    words = input()
    arlistinput.append(words)
    
arlistinput.remove('DONE')     # Removes 'DONE' from list that would have been automatically appended in the while loop.
#print(arlistinput)

print()
print('Unique list:')
 
for i in range (len(arlistinput)) :
     
    if arlistinput[i] not in array2:
        array2.append(arlistinput[i])


#printing final list
for k in range( len(array2)):         
    
    print(array2[k])    
""" dictionaries did not work.
    
for i in range ( len(arlistinput)-1,-1,-1):                    # YOU STOPPED HERE......
            
    if not arlistinput[i] in arlistfiltered:      #DICTIONARY
        
        
        arlistfiltered[arlistinput[i]] = 1
    else:
        arlistfiltered[arlistinput[i]] += 1
    
arlistinput= list(arlistfiltered.keys())     #== NEW LIST 


for i in range( len(arlistinput) ):
    
    print(arlistinput[i])        
        """