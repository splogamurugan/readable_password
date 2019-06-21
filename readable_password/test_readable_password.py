import unittest
import string
from .readable_password import readable_password
class ReadablePasswordTest(unittest.TestCase):

    def test_len(self):
        '''
        To test the length of the password
        '''
        self.assertEquals(len(readable_password(10)), 10)
        self.assertEquals(len(readable_password(3)), 6)
    
    def test_has_upper_case(self):
        self.assertEquals(str.istitle(readable_password(10)), True)
    
    def test_has_full_lower_case(self):
        self.assertEquals(str.islower(readable_password(10, incl_upper=False)), True)

    def test_has_numbers(self):
        password = readable_password(10)
        nums = [s for s in password if s in string.digits]
        self.assertGreaterEqual(len(nums), 1)

    def test_has_no_numbers(self):
        password = readable_password(10, incl_digit=False)
        nums = [s for s in password if s in string.digits]
        self.assertEqual(0, len(nums), msg="no numbers should present")
    
    def test_has_puncs(self):
        password = readable_password(10)
        nums = [s for s in password if s in string.punctuation]
        self.assertGreaterEqual(len(nums), 1)
    
    def test_has_no_puncs(self):
        password = readable_password(10, incl_punc=False)
        nums = [s for s in password if s in string.punctuation]
        self.assertEqual(0, len(nums), msg="no punctuation should present")
