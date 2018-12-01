prompt_distance = "How far did you run in miles? "
prompt_time = "How long were you running in hours? "
distance = float(input(prompt_distance))
time = float(input(prompt_time))
rate = distance / time
message = "You ran " + str(distance) + " miles at " + str(round(rate,2)) + " mph."
print(message)