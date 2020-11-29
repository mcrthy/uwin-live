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

class TestEmailPrefix(unittest.TestCase):
    def test_returns_email_prefix(self):
        """
        Test that it returns the email prefix
        """
        prefix = "mccarth7"
        email = "mccarth7@uwindsor.ca"
        result = get_email_prefix(email)
        self.assertEqual(prefix, result)
    
    def test_input_is_email(self):
        """
        Test that the input to the function is a valid email address
        """

        invalid_input = "This is not an email address"
        valid_input = "someone@something.com"
        prefix = "someone"

        result1 = get_email_prefix(invalid_input)
        result2 = get_email_prefix(valid_input)

        self.assertEqual(-1, result1)
        self.assertEqual(prefix, result2)


if __name__ == '__main__':
    unittest.main()