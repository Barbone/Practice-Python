def line_of(n, chrt='-'):
    '''Prints a line of n characters length'''

    def f_test(n):  # check the length of the line without additional message
        test = ''
        for u in range(n):
            test = test+'='
        print(test)

    if (type(chrt) != str or len(chrt) > 1 or chrt == ''):
        raise TypeError("The second arg must be a non empty unique character")
    if (type(n) != int or n <= 0):
        raise TypeError("The first arg must be an integer bigger than zero")
    if(n > 79):
        print("The recommended line of Python program is up to 79 characters")
    shir = ''
    lon = len(str(n))  # length of number
    lot = len('|<This is a string of  characters>|')  # length of text
    lom = lot+lon  # length of message text
    wing = int((n-lon-lom)/2)  # the length of characters side wing
    if (n == 1):
        characters = 'character'
    else:
        characters = 'characters'
    if (n > (lom+lon)):
        for m in range(wing+1):
            shir = shir + chrt
        if(n % 2 == 0):
            print('|<', shir, ' This is a line of ', n, ' characters ', shir, chrt, '>|', sep='')  # for even lengths we have to use asymetric wings of characters
        else:
            print('|<', shir, ' This is a line of ', n, ' characters ', shir, '>|', sep='')
#       f_test(n)
    elif(n >= 4):
        for m in range(n-4):
            shir = shir + chrt
        print("The following is a line of", n, characters)
        print('|<', shir, '>|', sep='')
#       f_test(n)

    else:
        for m in range(n):
            shir = shir + chrt
        print("The following is a line of", n, characters)
        print(shir)
#       f_test(n)
