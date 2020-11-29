import unittest

from lib import rand_int, get_email_prefix

class TestRandInt(unittest.TestCase):
    def test_returns_int(self):
        """
        Test that it returns an integer
        """
        test_obj = "This is a test object"
        result = rand_int(test_obj)
        self.assertIsInstance(result, int)

if __name__ == '__main__':
    unittest.main()