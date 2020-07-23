# place `import` statement at top of the program
import random

# don't modify this code or variable `n` may not be available
n = int(input())

# put your code here
my_seed = random.seed(n)
my_random = random.randint(-100, 100)
print(my_random)
