#program to create a histogram of marks using an array to store counter values
#victor gueorguiev
#20 april 2014

def main():
    xinput = input('Enter a space-separated list of marks:\n')
    marks_array = xinput.split(' ')
    counter_array = [0,0,0,0,0]
    for mark in marks_array:
        if 75<=int(mark)<=100:
            counter_array[0] += 1
        elif 70<=int(mark)<75:
            counter_array[1] += 1
        elif 60<=int(mark)<70:
            counter_array[2] += 1
        elif 50<=int(mark)<60:
            counter_array[3] += 1
        else: counter_array[4] += 1
    print('1 |'+'X'*counter_array[0])
    print('2+|'+'X'*counter_array[1])
    print('2-|'+'X'*counter_array[2])
    print('3 |'+'X'*counter_array[3])
    print('F |'+'X'*counter_array[4])
main()