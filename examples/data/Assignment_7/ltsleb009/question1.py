#-------------------------------------------------------------------------------#
# Name:        Question1                                                        #
# Purpose:     Assignment 7                                                     #
#                                                                               #
# Author:      Taylor                                                           #
#                                                                               #
# Created:     27/04/2014                                                       #
# Copyright:   (c) Taylor 2014                                                  #
#-------------------------------------------------------------------------------#

def duplicate():
	"""print list of strings without duplicates"""

	listofwords = [] #create a list
	string = input("Enter strings (end with DONE):\n")

	if string == "DONE":
		print("\nUnique list:")

	else:
		listofwords.append(string)
		while True:

			string = input()

			if string == "DONE":
				break
			if not string in listofwords: #if the current string is not in list of words, append it or if it is, continue program.

				listofwords.append(string)

		print("\nUnique list:")
		for word in listofwords: #iterate in the list of words and print them
			print(word)

duplicate()
