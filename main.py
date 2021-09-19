import time

print('Welcome to Sustainability vibes\nWe will help you to cook your food.\nOur recipes will help you cook just the'
      'right quantity of food and save the extra ingredients.\nThis will help the future generations since it will '
      'reduce the possibility of famines greatly and you will do your\n part in creating a sustainable future')
time.sleep(2)
x = int(input('What would you like today?\n 1)Breakfast\n 2)Lunch/Dinner\n 3)Drinks\n(Type the Serial Number of your '
              'choice): '))
print('reading input....')
time.sleep(2)
print(x)


def errorcode():
    print('Invalid Response. choose again.')
    selection()


def breakmenu():
    print('Breakfast Menu')
    with open('BreakFast.txt', 'r') as menu:
        fast = menu.read()
        print(fast)


def dinnermenu():
    print('Lunch/Dinner Menu')
    with open('Lunch Dinner.txt', 'r') as ld:
        fastd = ld.read()
        print(fastd)


def drinksmenu():
    print('Drinks Menu')
    with open('drinks.txt', 'r') as dr:
        ink = dr.read()
        print(ink)


def frenchtoast():
    with open('french.txt', 'r') as french:
        toast = french.read()
        print(toast)


def sandwich():
    with open('sand.txt', 'r') as sand:
        which = sand.read()
        print(which)


def oatscereals():
    with open('Oats and Cereals.txt', 'r') as oats:
        cereals = oats.read()
        print(cereals)


def butterchicken():
    with open('butterchicken.txt', 'r') as chik:
        butter = chik.read()
        print(butter)


def dal():
    with open('blackgram pulses (1).txt', 'r') as daal:
        makh = daal.read()
        print(makh)


def spaghetti():
    with open('Spagheti.txt', 'r') as pasta:
        cer = pasta.read()
        print(cer)


def biryani():
    with open('Spagheti.txt', 'r') as rice:
        non = rice.read()
        print(non)


def pulao():
    with open('veg biryani.txt', 'r') as ice:
        no = ice.read()
        print(no)


def salad():
    with open('nutsalad.txt', 'r') as nutsalad:
        nut = nutsalad.read()
        print(nut)


def coffee():
    with open('Coffee.txt', 'r') as coffe:
        cafe = coffe.read()
        print(cafe)


def tea():
    with open('Tea.txt', 'r') as teas:
        teak = teas.read()
        print(teak)


def mojito():
    with open('Mojito.txt', 'r') as moj:
        ito = moj.read()
        print(ito)


def lemonade():
    with open('lemonade.txt', 'r') as lemon:
        ade = lemon.read()
        print(ade)


def mocktail():
    with open('Mocktail.txt', 'r') as mock:
        tail = mock.read()
        print(tail)


def bingredients():
    breakmenu()
    k = int(input('Enter the Serial Number of the dish you would like: '))
    if k == 1:
        frenchtoast()
    elif k == 2:
        sandwich()
    elif k == 3:
        oatscereals()
    else:
        errorcode()


def lunch():
    dinnermenu()
    l = int(input('Enter the Serial Number of the dish you would like: '))
    if l == 1:
        butterchicken()
    elif l == 2:
        biryani()
    elif l == 3:
        pulao()
    elif l == 4:
        dal()
    elif l == 5:
        spaghetti()
    elif l == 6:
        salad()
    else:
        errorcode()


def drinks():
    drinksmenu()
    d = int(input('Enter the Serial Number of the dish you would like: '))
    if d == 1:
        mojito()
    elif d == 2:
        mocktail()
    elif d == 3:
        lemonade()
    elif d == 4:
        tea()
    elif d == 5:
        coffee()
    else:
        errorcode()


def selection():
    if x == 1:
        bingredients()

    elif x == 2:
        lunch()

    elif x == 3:
        drinks()

    else:
        print('Invalid Response. choose again.')


selection()
