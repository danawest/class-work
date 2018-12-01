prompt = "How many miles did you run? "
miles = float(input(prompt))
km = miles * 1.60934
message = "You ran " + str(round(miles,2)) + " miles, which is " + str(round(km,2)) + " kilometers!"
print(message)