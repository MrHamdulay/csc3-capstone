def string_align():
    names = []
    str_lens = []
    x = input("Enter strings (end with DONE):\n")
    names.append(x)
    while x != 'DONE':
        x = input()
        names.append(x)
    k = names.index('DONE')
    del names[k]
    for name in names:
        y = len(name)
        str_lens.append(y)
    str_lens.sort()
    print()
    print("Right-aligned list:")
    if len(str_lens)>0:
        align = str_lens[-1]
        
        
        for name in names:  
            print((align-len(name))*' ', name,sep = '')
string_align()