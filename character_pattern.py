# line < 100
# column < 100
def pattern():
    pattern_list = ['*', '$']
    while True:
        try:
            line, column = input('Dear user! Right two numbers between 0 and 99.\nRemember, it has to be integer split one whitespace. Look the exemple below:\n7 10\n20 100.\nFollow this exemple.\nOk. Let\'s do it.\n').split()
            if 0 < int(line) < 100 and 0 < int(column) < 100: #max number of column and row
                for i in range(int(line)): #number of rows
                    print()
                    for i in range(int(column)): #number of columns
                        for i in pattern_list: #iteration of the list of the given patterns
                            print(i, end='')
                print('\nGreat! You did it! This is your pattern above:)')
                break              
        except ValueError:
            print('wrong')

if __name__ == "__main__":
    pattern()




# Code try for the right pattern print
# pattern = ['o', 'x']
# for i in range(5): #row
#     print()
#     for i in range(5): #column
#         for i in pattern:
#             print(i, end='')