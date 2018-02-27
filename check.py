
def choice1(value1):
    if value1 == 'blk':
        x = 0
    elif value1=='brn':
        x = 1
    elif value1 =='r':
        x = 2
    elif value1 == 'o' :
        x = 3
    else:
        x = 4
    return int(x)

def choice2(value2):
    if value2 == 'blk':
        y = 0
    elif value2 =='brn':
        y = 1
    elif value2 == 'r' :
        y = 2
    elif value2 == 'o' :
        y = 3
    else:
        y = 4
    return int(y)

def choice3(value3):
    if value3 == 'blk':
        z = 0
    elif value3 == 'brn' :
        z = 1
    elif value3 == 'r' :
        z = 2
    elif value3 == 'o' :
        z = 3
    else:
        z = 4
    return int(z)

def value_calc():
    value1 = input("Enter the color(black (blk), brown (brn), red (r), orange(o), green (grn), blue (blu), violet (v), grey (gry), white (w)) : ")
    value2 = input("Enter the color(black (blk), brown (brn), red (r), orange(o), green (grn), blue (blu), violet (v), grey (gry), white (w)) : ")
    value3 = input("Enter the color(black (blk), brown (brn), red (r), orange(o), green (grn), blue (blu), violet (v), grey (gry), white (w)) : " )

    ohm = ((10*choice1(value1))+choice2(value2))* (10**choice3(value3))
    kohm = ohm/1000
    print(str(kohm) + " kohms")


value_calc()
