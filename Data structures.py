lunches = ["potato thing", "noodles", "rice", "beef", "chicken ","soup","chicken"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
rating = [7, 8, 6, 9, 3, 4, 8]
#print(lunches[1])                   #look up and element in an array

#linear searching is when we search for element one by one

def ex1():
    today = input("What day of the week is it?")
    for i in range(7):
        if days[i] == today:
            if rating[i] < 5:
                print("Food sucks, bring a packed lunch")

def rec():
    print("On these days, food is bad:")
    for i in range (7):
        if rating[i] < 5:
            print(days[i])

def manualcheck():
    today = input("What day is it?")
    today = today.lower()
    boolday = True
    while days == today:
        boolday = True
        break
    else:
        print("Wrong day")

manualcheck()
