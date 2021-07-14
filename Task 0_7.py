def celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32  # Converts temperature in Celsius to Fahrenheit
    return f


def fahrenheit_to_celsius(f):
    c = (f - 32) * 5 / 9  # Converts temperature in Fahrenheit to Celsius
    return c


fahrenheit_temp = celsius_to_fahrenheit(12)
print(f"Temperature in Farenheit: {fahrenheit_temp}")

celsius_temp = fahrenheit_to_celsius(32)
print(f"Temperature in Celsius: {celsius_temp}")
