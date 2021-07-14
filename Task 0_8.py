"""This function accepts a number and converts it to hours and minutes
"""


def hours_and_mins(number):
    hours = number // 60  # Converts number to hours
    mins = number % 60  # Converts number to minutes
    if hours <= 1 and mins <= 1:
        time = f"{number} is {hours} hour, {mins} minute"
    elif hours <= 1 and mins > 1:
        time = f"{number} is {hours} hour, {mins} minutes"
    elif hours > 1 and mins <= 1:
        time = f"{number} is {hours} hours, {mins} minute"
    else:
        time = f"{number} is {hours} hours, {mins} minutes"

    return time


print(hours_and_mins(0))
