def main():
    time = input("What time is it? ")
    converted = convert(time)
    if(converted>=7 and converted<=8):
        print("breakfast time")
    elif(converted>=12 and converted<=13):
        print("lunch time")
    elif(converted>=18 and converted<=19):
        print("dinner time")

def convert(time):
    hour,minute = time.split(":")
    minute = int(minute)/60
    return float(int(hour)+float(minute))

if __name__ == "__main__":
    main()
