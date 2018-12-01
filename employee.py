class Employee():
	"""A class to represent an employee."""

	def __init__(self, first_name, last_name, salary):
		"""Initialize the employee."""
		self.first = first_name.title()
		self.last = last_name.title()
		self.salary = salary

	def give_raise(self, amount=5000):
		"""Give the employee a raise."""
		self.salary += amount
