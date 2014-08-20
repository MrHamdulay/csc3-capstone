ifname = input("Enter the input filename:\n")
ofname = input("Enter the output filename:\n")
width = int(input("Enter the line width:\n"))

fin = open(ifname, "r")
fout = open(ofname, "w")

cur_len = 0
for line in fin.readlines():
    if line == "" or line == "\n":
        cur_len = 0
        fout.write("\n\n")
        continue

    for word in line.split(" "):
        if word == "\n":
            continue

        if word == "":
            fout.write(" ")
            cur_len += 1
            continue

        if word[-1] == "\n":
            word = word[:-1]

        if cur_len + len(word) > width:
            fout.write("\n" + word + " ")
            cur_len = len(word) + 1
        else:
            fout.write(word)
            if cur_len + len(word) < width:
                fout.write(" ")
                cur_len += 1
            cur_len += len(word)

        if cur_len == width:
            fout.write("\n")
            cur_len = 0
    
fout.write("\n")
