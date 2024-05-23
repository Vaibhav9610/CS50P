def main():
    time=input("What time is it: ")
    convert(time)

def convert(time):
    time=time.partition(":")
    time=float(time[0])+float(time[2])/60

    if 7<=time<=8:
        print("Breakfast Time")
    elif 12<=time<=13:
        print("Lunch Time")
    elif 18<=time<=19:
        print("Dinner Time")

main()