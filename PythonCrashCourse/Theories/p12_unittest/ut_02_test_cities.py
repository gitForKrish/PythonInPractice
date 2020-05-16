import unittest
from ut_02_city_functions import show_cities

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        city_info = show_cities('bangalore', 'india')
        self.assertEqual(city_info, 'Bangalore India')

    def test_city_country_population(self):
        city_info = show_cities('bangalore','india', 4000000)
        self.assertEqual(city_info, 'Bangalore India - population 4000000')
        
if __name__ == "__main__":
    unittest.main()