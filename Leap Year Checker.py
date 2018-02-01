
def noleap():
    print("Not a leap year")

year = int(input("Gimme a year to check"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            noleap()
    else:
        noleap()
else:
    noleap()


