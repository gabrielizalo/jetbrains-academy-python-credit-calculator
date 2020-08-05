import math

my_int = int(input())

sigmoid = math.exp(my_int) / (math.exp(my_int) + 1)

print(round(sigmoid, 2))
