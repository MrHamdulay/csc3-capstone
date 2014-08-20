'''program to take a text file and edit it so that each line has the specified width
Wandile Khowa
11-05-2014
'''
import textwrap
def text_editer(a, b, c):
    file_in = open(a, "r")
    file_out = open(b, "w")
    whole_file_in = file_in.read()
    dedented_text = textwrap.dedent(whole_file_in).strip()
    for width in [c]:
        print()
        print (textwrap.fill(dedented_text, width=width), file=file_out)
            
    file_in.close()
    file_out.close()    
                    
def main():
    in_file = input("Enter the input filename: \n")
    out_file = input("Enter the output filename: \n")
    width = eval(input("Enter the line width: \n"))
    text_editer(in_file, out_file, width)
    
if __name__=='__main__':
    main()
    