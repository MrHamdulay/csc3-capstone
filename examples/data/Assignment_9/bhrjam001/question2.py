# Assignment 9 Question 2
# James Behr
# 2014-05-12

# User input
f = open(input('Enter the input filename:\n'))
output = open(input('Enter the output filename:\n'), 'w')
linelength = int(input('Enter the line width:\n'))


# Read file into a list paragraphs, by splitting by two consecutive blank lines
paragraphs = f.read().split('\n\n')

# Replace the newlines in each paragraph by a single space.
for i, paragraph in enumerate(paragraphs):
    paragraphs[i] = paragraph.replace('\n', ' ')

# Loop over each paragraph
for paragraph in paragraphs:
    # Use a while loop for a variable step on counter 'i'
    i = 0
    while i <= len(paragraph):
        # Seperate the paragraph into lines exactly 'linelength' characters long
        roughline = paragraph[i:i + linelength + 1]
        
        # Reverse search for a space if the line is too long and record that point
        lastspace = roughline.rfind(' ') if len(roughline) >= linelength else linelength
        
        if lastspace > 0:
            # If there was a found space, split the paragraph at that point
            print(paragraph[i:i + lastspace + 1].strip(), file = output)
            # Jump forward the amount of text processed
            i += lastspace + 1
            
        else:
            # Otherwise just copy the full line (this will cause truncatation)
            print(roughline.strip(), file = output)
            # Jump forward a fixed amount (we don't want to jump forward -1)
            i += linelength
            
    #Print a blank line after each paragraph
    print(file = output) 
    
# Close the files        
f.close()
output.close()