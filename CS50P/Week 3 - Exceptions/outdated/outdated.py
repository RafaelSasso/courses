def main():
    while True:
        try:
            date = input("Date: ")
            print(convert(date.title().strip()))
            return
        except ValueError:
            pass

def convert(date):
    months = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November","December"
    ]

    if( "/" in date):
        month, day, year = date.split("/")
    else:
        month, day , year = date.split(" ")
        if (month not in months):
            raise ValueError
        for i in range(len(months)):
            if months[i] == month:
                month = str(i+1)

        day,_ = day.split(",")

    if len(day)<2:
        day = "0"+day

    if len(month)<2:
        month = "0"+month

    if not(0<int(month)<=12 and 0<int(day)<=31):
        raise ValueError

    new = (f"{year}-{month}-{day}")


    return new

main()
