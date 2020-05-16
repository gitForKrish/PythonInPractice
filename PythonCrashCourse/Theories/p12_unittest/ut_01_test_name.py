import unittest
from ut_01_namefunc import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('william', 'jackson')
        self.assertEqual(formatted_name, 'William Jackson')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('tarun', 'mandal','kumar')
        self.assertEqual(formatted_name, 'Tarun Kumar Mandal')

if __name__ == "__main__":
    unittest.main()