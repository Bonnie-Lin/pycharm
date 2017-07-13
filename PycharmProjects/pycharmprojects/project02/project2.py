#tic tac toe game
empty = [1,2,3,4,5,6,7,8,9]
used = []
def putdown():
    firstrow = '_1_|_2_|_3_'
    secondrow = '_4_|_5_|_6_'
    thirdrow = '_7_|_8_|_9_'
    print (firstrow)
    print (secondrow)
    print (thirdrow)

    playerinput = input('pick a number')
    #playerinput = int(playerinput)
    index = int(playerinput) - 1
    used.append(empty[index])
    print (empty)
    print (used)

    for characters in firstrow or secondrow or thirdrow:
        grid = firstrow, secondrow, thirdrow
        if playerinput in firstrow:

            firstrow = firstrow.replace(playerinput, 'o')
            print (firstrow)
            print (secondrow)
            print (thirdrow)
            grid = firstrow, secondrow, thirdrow
            return grid
        if playerinput in secondrow:
            secondrow = secondrow.replace(playerinput, 'o')
            print(firstrow)
            print(secondrow)
            print(thirdrow)
            grid = firstrow, secondrow, thirdrow
            return grid
        if playerinput in thirdrow:
            thirdrow = thirdrow.replace(playerinput, 'o')
            print(firstrow)
            print(secondrow)
            print(thirdrow)
            grid = firstrow, secondrow, thirdrow
            return grid
putdown()
putdown()





