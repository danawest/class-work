prompt = "What is the temperature in degrees Fahrenheit? "
fahrenheit = float(input(prompt))
celsius = (fahrenheit - 32) / 1.8
message = "The temperature " + str(fahrenheit) + " degrees Fahrenheit is " + str(round(celsius,2)) + " degrees Celsius."
print(message)