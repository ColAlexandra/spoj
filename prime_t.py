these = True
while these:
    i = int(input())
    if i <= 10000:
        these = False
        if i == 2 or i == 3 or i ==5:
            print('TAK')
        elif i % 1 == 0 and i % i == 0 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            print('TAK')
        else:
            print('NIE')
    elif i > 10000:
        print('Wrong number')

