import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test for the module employee."""

	def setUp(self):
		"""Make up a test employee"""
		self.dana = Employee('dana', 'west', 50000)

	def test_give_default_raise(self):
		"""Test that the default value for 'raise' works."""
		self.dana.give_raise()
		self.assertEqual(self.dana.salary, 55000)

	def test_give_custom_raise(self):
		"""Try giving the employee a custom raise."""
		self.dana.give_raise(7500)
		self.assertEqual(self.dana.salary, 57500)

unittest.main()