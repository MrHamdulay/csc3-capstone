x = eval(input("Enter the height of the triangle:\n"))
y = 0
while y < x:
	numStars = (2*y + 1)
	stars = "*"*numStars
	print(" "*(x-y-1)+stars)
	y+=1


'''
Enter the height of the triangle:
5
    *
   ***
  *****
 *******
*********
'''
