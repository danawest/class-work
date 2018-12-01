birds = ['crow', 'sparrow', 'gull', 'hawk']
print("The following is a list with something in common:")
for bird in birds:
	print(bird)

prompt = "Add a similar item to the list: "
favorite_bird = input(prompt)
birds.append(favorite_bird)
print("Good job! You added another bird to the list!")
for bird in birds:
	print(bird)