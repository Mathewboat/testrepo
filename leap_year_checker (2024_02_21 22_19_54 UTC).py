def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            print("Leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")

entry = int(input("Enter a year: "))
is_leap_year(entry)
