import unittest
from src import parcel_parser


class TestClassifyParcel(unittest.TestCase):
    """ Test cases on parcel classification """

    @classmethod
    def setUpClass(cls):
        cls.parser = parcel_parser.ParcelParser()

    """ Small packages """

    def test_classify_parcel_small(self):
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['small']['height'])
        weight = float(self.parser.package_data['small']['weight'])
        parcel = self.parser._classify_parcel(length, breadth, height, weight)

        self.assertEqual(self.parser.package_data['small']['cost'], parcel.cost)
        self.assertEqual('small', parcel.package_type)

    def test_classify_parcel_small_overweight(self):
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['small']['height'])
        weight = float(self.parser.package_data['small']['weight'] + 1)

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser._classify_parcel(length, breadth, height, weight)

    """ Medium packages """

    def test_classify_parcel_medium_length(self):
        length = float(self.parser.package_data['medium']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['small']['height'])
        weight = float(self.parser.package_data['medium']['weight'])
        parcel = self.parser._classify_parcel(length, breadth, height, weight)

        self.assertEqual(self.parser.package_data['medium']['cost'], parcel.cost)
        self.assertEqual('medium', parcel.package_type)

    def test_classify_parcel_medium_breadth(self):
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['medium']['breadth'])
        height = float(self.parser.package_data['small']['height'])
        weight = float(self.parser.package_data['medium']['weight'])
        parcel = self.parser._classify_parcel(length, breadth, height, weight)

        self.assertEqual(self.parser.package_data['medium']['cost'], parcel.cost)
        self.assertEqual('medium', parcel.package_type)

    def test_classify_parcel_medium_height(self):
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['medium']['height'])
        weight = float(self.parser.package_data['medium']['weight'])
        parcel = self.parser._classify_parcel(length, breadth, height, weight)

        self.assertEqual(self.parser.package_data['medium']['cost'], parcel.cost)
        self.assertEqual('medium', parcel.package_type)

    def test_classify_parcel_medium_overweight(self):
        length = float(self.parser.package_data['medium']['length'])
        breadth = float(self.parser.package_data['medium']['breadth'])
        height = float(self.parser.package_data['medium']['height'])
        weight = float(self.parser.package_data['medium']['weight'] + 1)

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser._classify_parcel(length, breadth, height, weight)

    """ Large packages """

    def test_classify_parcel_large_length(self):
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['small']['height'])
        weight = float(self.parser.package_data['large']['weight'])
        parcel = self.parser._classify_parcel(length, breadth, height, weight)

        self.assertEqual(self.parser.package_data['large']['cost'], parcel.cost)
        self.assertEqual('large', parcel.package_type)

    def test_classify_parcel_large_breadth(self):
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['small']['height'])
        weight = float(self.parser.package_data['large']['weight'])
        parcel = self.parser._classify_parcel(length, breadth, height, weight)

        self.assertEqual(self.parser.package_data['large']['cost'], parcel.cost)
        self.assertEqual('large', parcel.package_type)

    def test_classify_parcel_large_height(self):
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['large']['height'])
        weight = float(self.parser.package_data['large']['weight'])
        parcel = self.parser._classify_parcel(length, breadth, height, weight)

        self.assertEqual(self.parser.package_data['large']['cost'], parcel.cost)
        self.assertEqual('large', parcel.package_type)

    def test_classify_parcel_large_overweight(self):
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])
        weight = float(self.parser.package_data['large']['weight'] + 1)

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser._classify_parcel(length, breadth, height, weight)

    """ Oversize packages """

    def test_classify_parcel_oversize_length(self):
        length = float(self.parser.package_data['large']['length']) + 1
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])
        weight = float(self.parser.package_data['large']['weight'])

        with self.assertRaisesRegex(parcel_parser.ParcelOversizeError, 'Parcel length exceeded maximum limit'):
            self.parser._classify_parcel(length, breadth, height, weight)

    def test_classify_parcel_oversize_breadth(self):
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth']) + 1
        height = float(self.parser.package_data['large']['height'])
        weight = float(self.parser.package_data['large']['weight'])

        with self.assertRaisesRegex(parcel_parser.ParcelOversizeError, 'Parcel breadth exceeded maximum limit'):
            self.parser._classify_parcel(length, breadth, height, weight)

    def test_classify_parcel_oversize_height(self):
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height']) + 1
        weight = float(self.parser.package_data['large']['weight'])

        with self.assertRaisesRegex(parcel_parser.ParcelOversizeError, 'Parcel height exceeded maximum limit'):
            self.parser._classify_parcel(length, breadth, height, weight)


if __name__ == '__main__':
    unittest.main()
