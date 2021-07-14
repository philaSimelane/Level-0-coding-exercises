import math


def area_of_triangle(side1, side2, side3):
    s = 1 / 2 * (side1 + side2 + side3)  # calculate semiperimeter of a triangle
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))  # area of triangle
    return area


Area = area_of_triangle(3, 4, 5)
print(f"Area of triangle: {Area}")
