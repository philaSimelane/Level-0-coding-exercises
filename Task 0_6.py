def maximum(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


max_value = maximum(3, 5, 4)
print(f"Maximum value: {max_value}")

