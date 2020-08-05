import math

angle_degrees = int(input())
angle_radians = math.radians(angle_degrees)
cotangent = math.cos(angle_radians) / math.sin(angle_radians)

print(round(cotangent, 10))
