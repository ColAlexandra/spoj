#number between 0 and 200, every input in another line, give the sum

conv = True
while conv:
    try:
        num1 = int(input())
        num2 = int(input())
        if num1 <=200 and num2<=200:
            sum = num1 + num2
            print(sum)
            conv = False
        else: 
            print('Every number sholud be between 0 and 200')
    except ValueError:
        print('Wrong number, try again')