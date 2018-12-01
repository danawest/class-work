import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    def test_city_country(self):
        """Does a city and country pair work?"""
        dublin_ireland = city_country('dublin', 'ireland')
        self.assertEqual(dublin_ireland, 'Dublin, Ireland')
    def test_city_country_population(self):
    	"""Does it still work if a population is included?"""
    	dublin_ireland = city_country('dublin', 'ireland', population=500000)
    	self.assertEqual(dublin_ireland, 'Dublin, Ireland - Population 500000')
unittest.main()