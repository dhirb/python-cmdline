import unittest
from mock import patch, mock_open
import random
from src import parcel_parser


class TestConfig(unittest.TestCase):
    """ Test cases on config files """

    @classmethod
    def setUpClass(cls):
        cls.parser = parcel_parser.ParcelParser()

    """ Packages config """

    def test_missing_packages_config(self):
        with self.assertRaises(FileNotFoundError):
            self.parser._get_package_data('../..')

    @patch("builtins.open", new_callable=mock_open, read_data='')
    def test_empty_packages_config(self, _):
        with self.assertRaisesRegex(parcel_parser.InvalidConfigError, 'Error: Package config file is empty'):
            self.parser._get_package_data('config/')

    def test_setup_packages_non_numeric_length(self):
        data = {'small': {'length': 'abc', 'breadth': 300, 'height': 150, 'weight': 25, 'cost': 5.0}}

        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: length must be numeric'):
            self.parser._setup_packages(data)

    def test_setup_packages_non_numeric_breadth(self):
        data = {'small': {'length': 200, 'breadth': 'abc', 'height': 150, 'weight': 25, 'cost': 5.0}}

        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: breadth must be numeric'):
            self.parser._setup_packages(data)

    def test_setup_packages_non_numeric_height(self):
        data = {'small': {'length': 200, 'breadth': 300, 'height': 'abc', 'weight': 25, 'cost': 5.0}}

        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: height must be numeric'):
            self.parser._setup_packages(data)

    def test_setup_packages_non_numeric_weight(self):
        data = {'small': {'length': 200, 'breadth': 300, 'height': 150, 'weight': 'abc', 'cost': 5.0}}

        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: weight must be numeric'):
            self.parser._setup_packages(data)

    def test_setup_packages_non_numeric_cost(self):
        data = {'small': {'length': 200, 'breadth': 300, 'height': 150, 'weight': 25, 'cost': 'abc'}}

        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: cost must be numeric'):
            self.parser._setup_packages(data)

    def test_setup_packages_missing_length(self):
        data = {'small': {'breadth': 300, 'height': 150, 'weight': 25, 'cost': 5.0}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Missing \'length\' key in packages config file'):
            self.parser._setup_packages(data)

    def test_setup_packages_missing_breadth(self):
        data = {'small': {'length': 200, 'height': 150, 'weight': 25, 'cost': 5.0}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Missing \'breadth\' key in packages config file'):
            self.parser._setup_packages(data)

    def test_setup_packages_missing_height(self):
        data = {'small': {'length': 200, 'breadth': 300, 'weight': 25, 'cost': 5.0}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Missing \'height\' key in packages config file'):
            self.parser._setup_packages(data)

    def test_setup_packages_missing_weight(self):
        data = {'small': {'length': 200, 'breadth': 300, 'height': 150, 'cost': 5.0}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Missing \'weight\' key in packages config file'):
            self.parser._setup_packages(data)

    def test_setup_packages_missing_cost(self):
        data = {'small': {'length': 200, 'breadth': 300, 'height': 150, 'weight': 25}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Missing \'cost\' key in packages config file'):
            self.parser._setup_packages(data)

    def test_setup_packages_negative_cost(self):
        data = {'small': {'length': 200, 'breadth': 300, 'height': 150, 'weight': 25, 'cost': -1}}

        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: cost must be positive'):
            self.parser._setup_packages(data)

    def test_setup_packages_zero_cost(self):
        data = {'small': {'length': 200, 'breadth': 300, 'height': 150, 'weight': 25, 'cost': 0}}

        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: cost must be positive'):
            self.parser._setup_packages(data)

    def test_setup_packages_very_large_cost(self):
        data = {'small': {'length': 200, 'breadth': 300, 'height': 150, 'weight': 25, 'cost': random.getrandbits(9999)}}

        with self.assertRaisesRegex(parcel_parser.InvalidAttributeError, 'Error: cost must be within numerical limit'):
            self.parser._setup_packages(data)

    """ Conversion config """

    def test_missing_conversion_config(self):
        with self.assertRaises(FileNotFoundError):
            self.parser._setup_conversion_scale('../..')

    @patch("builtins.open", new_callable=mock_open, read_data='')
    def test_empty_conversion_config(self, _):
        with self.assertRaisesRegex(parcel_parser.InvalidConfigError, 'Error: Conversion config file is empty'):
            self.parser._setup_conversion_scale('config/')

    def test_setup_conversion_factors_non_numeric_mm(self):
        data = {'size': {'mm': 'abc', 'cm': 10, 'inch': 25.4}, 'weight': {'kg': 1, 'g': 0.001, 'lb': 0.453592}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Conversion config file contains invalid numeric parameter'):
            self.parser.conversion_scale = data
            self.parser._setup_conversion_factors('mm', 'kg')

    def test_setup_conversion_factors_non_numeric_cm(self):
        data = {'size': {'mm': 1, 'cm': 'abc', 'inch': 25.4}, 'weight': {'kg': 1, 'g': 0.001, 'lb': 0.453592}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Conversion config file contains invalid numeric parameter'):
            self.parser.conversion_scale = data
            self.parser._setup_conversion_factors('cm', 'kg')

    def test_setup_conversion_factors_non_numeric_inch(self):
        data = {'size': {'mm': 1, 'cm': 10, 'inch': 'abc'}, 'weight': {'kg': 1, 'g': 0.001, 'lb': 0.453592}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Conversion config file contains invalid numeric parameter'):
            self.parser.conversion_scale = data
            self.parser._setup_conversion_factors('inch', 'kg')

    def test_setup_conversion_factors_non_numeric_kg(self):
        data = {'size': {'mm': 1, 'cm': 10, 'inch': 25.4}, 'weight': {'kg': 'abc', 'g': 0.001, 'lb': 0.453592}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Conversion config file contains invalid numeric parameter'):
            self.parser.conversion_scale = data
            self.parser._setup_conversion_factors('mm', 'kg')

    def test_setup_conversion_factors_non_numeric_g(self):
        data = {'size': {'mm': 1, 'cm': 10, 'inch': 25.4}, 'weight': {'kg': 1, 'g': 'abc', 'lb': 0.453592}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Conversion config file contains invalid numeric parameter'):
            self.parser.conversion_scale = data
            self.parser._setup_conversion_factors('mm', 'g')

    def test_setup_conversion_factors_non_numeric_lb(self):
        data = {'size': {'mm': 1, 'cm': 10, 'inch': 25.4}, 'weight': {'kg': 1, 'g': 0.001, 'lb': 'abc'}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Conversion config file contains invalid numeric parameter'):
            self.parser.conversion_scale = data
            self.parser._setup_conversion_factors('mm', 'lb')

    def test_setup_conversion_factors_very_large_value(self):
        data = {'size': {'mm': random.getrandbits(9999), 'cm': 10, 'inch': 25.4},
                'weight': {'kg': 1, 'g': 0.001, 'lb': 'abc'}}

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError,
                                    'Error: Config field value must be within numerical limit'):
            self.parser.conversion_scale = data
            self.parser._setup_conversion_factors('mm', 'kg')
