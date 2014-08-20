# Proram to check the number of double cha(rr)acters in a string
# Mutali Mashamba
# [day] May 2014

msg=input('Enter a message:\n')

def doubles(string):
    count = 0
    if len(string) < 2:
        return count
    elif string[0] == string[1] :
        count += 1
        return count + doubles(string[2:])
    else :
        return count + doubles(string[1:])


print('Number of pairs:', doubles(msg))
