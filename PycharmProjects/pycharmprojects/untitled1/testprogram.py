print ('hello world')
def function():
    print ('ayo')

function()
y = input('enter name')

def otherfunction():
    if y == 'bonnie':
        print ('ayo man')
        return True
    else:
        print ('nope')
        exit()

otherfunction()

if otherfunction() == True:
    print ('awesome!')