"""James Godlonton
String formatter
10 May 2014"""

def formatT(text1,length,text2):
    """formatting function thats input text to format and length of each line them returns formatted string"""
    if len(text1)<length+1:#Exit statement if there is less then length number of characters in text
        text2=text2+text1
        return text2#Returns new text
    count=0
    while text1[length-1-count]!=" ":#While last letter is not a space keep adding to count so that we find the first space under length characters
        count=count+1
    text2=text2+text1[0:length-count]+"\n"#Split string according to how many fit on the line then add to new string with a next line 
    text1=text1[length-count:]#Cut the edited bit off first text
    return formatT(text1,length,text2)#Go through another recursion of statement with shortened text one and formatted text2

def main():
    """Main function for input output management """
    #getting input from user about filenames and length of each line
    inFile=input("Enter the input filename:\n")
    outFile=input("Enter the output filename:\n")
    linewidth=int(input("Enter the line width:\n"))
    
    f=open(inFile,"r")#open file
    text1=f.read()#read entire file
    f.close()#close file asap
    text1=text1.split("\n\n")#create a list of each paragraph
    outputT=""
    for i in range (len(text1)):#go through each paragraph format then add to output string
        text1[i]=text1[i].replace(" \n"," ")#getting rid of next line statements but not losing where there should be a space
        text1[i]=text1[i].replace("\n "," ")
        text1[i]=text1[i].replace("\n"," ")
        outputT=outputT+formatT(text1[i],linewidth+1,"")+"\n\n"#Format paragraph and then add to output with 2 next line args 
    out=open(outFile,"w")#open output file
    out.write(outputT)#output formatted string
    out.close()#close file
if __name__ == "__main__":
    main()
    
    
    
        
    