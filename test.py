# Input:
# 1
# 2
# 88
# 42
# 99

# Output:
# 1
# 2
# 88

import os
from time import sleep

while True:
    numbers = int(input())
    if numbers == 42:
        break
    print(numbers) 
    sleep(2)
    os.system('clear')