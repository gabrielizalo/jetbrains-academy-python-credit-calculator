import math

first_int = int(input())
second_int = int(input())
result = None

if second_int <= 1:
    result = math.log(first_int)
else:
    result = math.log(first_int, second_int)

print(round(result, 2))
