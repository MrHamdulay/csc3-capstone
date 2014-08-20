"""A program to count the number of pairs of repeated characters in a string.
Simlindile Mahlaba
09 May 2014"""

def rep_letters(str_1, list_1, count):
    if len(str_1)>0:
        if len(list_1)==0:
            list_1.append(str_1[0])
        elif str_1[0]!=list_1[len(list_1)-1]:
            list_1.append(str_1[0])
        else:
            if  str_1[0]==list_1[len(list_1)-1]:
                list_1.remove(str_1[0])
                count+=1
        str_1=str_1[1:len(str_1)]
        return rep_letters(str_1, list_1, count)
    if len(str_1)==0:
        return count

def main():
    str_1=input("Enter a message:\n")
    list_1=[]
    count=0
    print("Number of pairs:",rep_letters(str_1, list_1, count))
main()
