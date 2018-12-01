pizzas = ['hawaiian', 'pepperoni', 'plain cheese']
friend_pizzas = pizzas[:]

print("My favorite pizzas are:")
print(pizzas)

print("My friend's favorite pizzas are:")
print(friend_pizzas)

pizzas.append('pesto')
friend_pizzas.append('sausage')

for pizza in pizzas:
	print("I like " + pizza + " pizza.")
	
for friend_pizza in friend_pizzas:
	print("My friend likes " + friend_pizza + " pizza.")
	