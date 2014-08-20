'''This program formats a given string from a file
By Kouame Hermann KOUASSI: KSSKOU001
On 15 May 2014'''

def print_word(lines, width, f):
        new_width = width
        for line_no in range(len(lines)):
                if lines[line_no][-1] == '\n' and lines[line_no] != '\n':
                        lines[line_no] = lines[line_no][:-1]
                if lines[line_no] == '\n' :
                        print('\n', file = f)
                        new_width = width
                else:
                        list_word = lines[line_no].split(' ')
                        for word_no in range(len(list_word)):
                                if len(list_word[word_no]) <= new_width :
                                        new_width -= len(list_word[word_no]) + 1
                                        if list_word[word_no] != list_word[-1]:
                                                if len(list_word[word_no + 1]) <= new_width:
                                                        print(list_word[word_no], ' ', sep = '', end = '', file = f)
                                                else:                     
                                                        print(list_word[word_no], file = f)
                                                        new_width = width
                                        else:
                                                if lines[line_no] != lines[-1]:
                                                        next_line = lines[line_no + 1]
                                                        next_word = next_line.split(' ')[0]        
                                                        if len(next_word) <= new_width :
                                                                print(list_word[word_no], ' ', sep ='', end = '', file = f)
                                                        else:
                                                                print(list_word[word_no], file = f)
                                                                new_width = width                                                        
                                                else:
                                                        print(list_word[word_no], file = f)                
                

def main():
        in_file = input('Enter the input filename:\n')
        in_f = open(in_file, 'r')
        lines = in_f.readlines()
        out_file = input('Enter the output filename:\n')
        width = eval(input('Enter the line width:\n'))
        out_f = open(out_file, 'w')
        print_word(lines, width, out_f)
        in_f.close()
                                
if __name__=="__main__":
        main()
                
        
        
