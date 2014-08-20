def time():
    start_hours,stop_hours=0,23
    start_minutes,stop_minutes=0,59
    start_seconds,stop_seconds=0,59
    hours= eval(input ("Enter the hours:\n"))
    minutes= eval(input ("Enter the minutes:\n"))
    seconds= eval(input ("Enter the seconds:\n"))
    if hours>=0 and hours<=23 and minutes>=0 and minutes<=59 and seconds>=0 and seconds<=59:
        print ("Your time is valid.")
    else: 
        print ("Your time is invalid.")
time()
