tryAgain = True
import datetime
now = datetime.datetime.now()


yearlist = [230,1999,2018,4096,1986,2020,512,2054,1837,1945,1360,3000,2048,1066,4,930,1024,32]

def yearchecker():
    global now
    if year < now.year:
        print(year,"was a leap year")
    elif year > now.year:
        print(year,"will be a leap year")
    elif year == now.year:
        print("This year is a leap year")

def noleap():
    print("Not a leap year")
def yesleap():
    print("Leap Year")

def leapyear():
    if year % 4 and year % 100 != 0:
        yearchecker()
    elif year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            yearchecker()




def checkarray():
    global yearlist
    global year
    for year in yearlist:
        leapyear()

checkarray()
