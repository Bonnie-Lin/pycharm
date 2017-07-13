
def dates():
    maxyear = input('max year you want')
    minyear = input('minimum date year you want')
    date = 1
    month = 1
    year = minyear
    time = date, "/", month, "/", year
    print('okay start')

    if month == int(1) or int(3) or int(5) or int(7) or int(8) or int(10) or int(12):
        while date <= 31:
            date = date + 1
    if month == int(4) or int(6) or int(9) or int(11):
        while date <= 30:
            date = date + 1
    if month == int(2):
        while date <= 28:
            date =  date + 1
    print (date, "is the dates")

    if month == int(1) or int(3) or int(5) or int(7) or int(8) or int(10) or int(12):
        if date == 31:
            month = month + 1
    if month == int(4) or int(6) or int(9) or int(11):
        if date == 30:
            month = month + 1
    if month == int(2):
        if date == 28:
            month = month + 1
    if month == int(12):
        while year <= maxyear:
            year = year + 1


    timelist = []
    timelistback = []
    alltimelist =[]
    for letters in time:
        timelist.append(letters)
        length = len(timelist)
        index = int(len(timelist) - 1)
        while int(length) <= len(timelist) and index >= 0:

            timelistback.append(timelist[index])
            index = index - 1
        if timelist == timelistback:
            print ('yay')
            alltimelist.append(time)
    print (time)
    print (alltimelist)

dates()
# def palindrome():
#     userinputlist2 = []
#     userinput = raw_input("Enter a string!")
#     userinputlist = []
#     for letters in userinput:
#         userinputlist.append(letters)
#
#         length = len(userinputlist)
#         userinputlist2 = [letters] + userinputlist2
#     if userinputlist == userinputlist2:
#         print
#         "Your string is a palindrome"
#     else:
#         print
#         "Your string is not a palindrome"
#     print
#     "your word backwards is:"
#     print
#     userinputlist2