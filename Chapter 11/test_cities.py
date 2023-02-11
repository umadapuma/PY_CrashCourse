#11-2 Population:
import unittest
from city_functions import location

class NamesTestCase(unittest.TestCase):

    def test_city_country(self):
        location_combine = location('santiago','chile')
        self.assertEqual(location_combine,'Santiago, Chile')
    
    def test_city_country_population(self):
        location_combine = location('santiago','chile','5000000')
        self.assertEqual(location_combine,'Santiago, Chile population - 5000000')

if __name__ == '__main__':
    unittest.main()