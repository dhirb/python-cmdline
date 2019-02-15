import unittest
import random
from src import parcel_parser


class TestValidate(unittest.TestCase):
    """ Test cases on numeric validation """

    @classmethod
    def setUpClass(cls):
        cls.parser = parcel_parser.ParcelParser()

    def test_validate_int(self):
        self.parser._validate_numeric(1, '')

    def test_validate_float(self):
        self.parser._validate_numeric(1.1, '')

    def test_validate_int_string(self):
        self.parser._validate_numeric('1', '')

    def test_validate_float_string(self):
        self.parser._validate_numeric('1.1', '')

    def test_validate_int_string_with_whitespace(self):
        self.parser._validate_numeric(' \n1\t', '')

    def test_validate_float_string_with_whitespace(self):
        self.parser._validate_numeric(' \n1.1\t', '')

    def test_validate_negative_param(self):
        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: length must be positive'):
            self.parser._validate_numeric(-1, 'length')

    def test_validate_zero_param(self):
        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: length must be positive'):
            self.parser._validate_numeric(0, 'length')

    def test_validate_non_numeric_param(self):
        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: length must be numeric'):
            self.parser._validate_numeric('abc', 'length')

    def test_validate_empty_whitespace_param(self):
        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: length must be numeric'):
            self.parser._validate_numeric(' ', 'length')

    def test_validate_param_with_whitespace(self):
        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: length must be numeric'):
            self.parser._validate_numeric(' 1 2 3 ', 'length')

    def test_validate_very_large_param(self):
        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError,
                                    'Error: length must be within numerical limit'):
            self.parser._validate_numeric(random.getrandbits(9999), 'length')


if __name__ == '__main__':
    unittest.main()
