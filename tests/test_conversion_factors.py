import unittest
from src import parcel_parser


class TestConversionFactors(unittest.TestCase):
    """ Test cases on conversion scale """

    @classmethod
    def setUpClass(cls):
        cls.parser = parcel_parser.ParcelParser()

    """ Small packages """

    def test_classify_parcel_small_in_mm(self):
        size_factor = float(self.parser.conversion_scale['size']['mm'])
        length = float(self.parser.package_data['small']['length']) / size_factor
        breadth = float(self.parser.package_data['small']['breadth']) / size_factor
        height = float(self.parser.package_data['small']['height']) / size_factor
        weight = float(self.parser.package_data['small']['weight'])
        parcel = self.parser.calculate(length, breadth, height, weight, size_unit='mm')

        self.assertEqual(self.parser.package_data['small']['cost'], parcel.cost)
        self.assertEqual('small', parcel.package_type)

    def test_classify_parcel_small_in_cm(self):
        size_factor = float(self.parser.conversion_scale['size']['cm'])
        length = float(self.parser.package_data['small']['length']) / size_factor
        breadth = float(self.parser.package_data['small']['breadth']) / size_factor
        height = float(self.parser.package_data['small']['height']) / size_factor
        weight = float(self.parser.package_data['small']['weight'])
        parcel = self.parser.calculate(length, breadth, height, weight, size_unit='cm')

        self.assertEqual(self.parser.package_data['small']['cost'], parcel.cost)
        self.assertEqual('small', parcel.package_type)

    def test_classify_parcel_small_in_inch(self):
        size_factor = float(self.parser.conversion_scale['size']['inch'])
        length = float(self.parser.package_data['small']['length']) / size_factor
        breadth = float(self.parser.package_data['small']['breadth']) / size_factor
        height = float(self.parser.package_data['small']['height']) / size_factor
        weight = float(self.parser.package_data['small']['weight'])
        parcel = self.parser.calculate(length, breadth, height, weight, size_unit='inch')

        self.assertEqual(self.parser.package_data['small']['cost'], parcel.cost)
        self.assertEqual('small', parcel.package_type)

    def test_classify_parcel_small_in_kg(self):
        weight_factor = float(self.parser.conversion_scale['weight']['kg'])
        weight = float(self.parser.package_data['small']['weight']) / weight_factor
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['small']['height'])
        parcel = self.parser.calculate(length, breadth, height, weight, weight_unit='kg')

        self.assertEqual(self.parser.package_data['small']['cost'], parcel.cost)
        self.assertEqual('small', parcel.package_type)

    def test_classify_parcel_small_in_g(self):
        weight_factor = float(self.parser.conversion_scale['weight']['g'])
        weight = float(self.parser.package_data['small']['weight']) / weight_factor
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['small']['height'])
        parcel = self.parser.calculate(length, breadth, height, weight, weight_unit='g')

        self.assertEqual(self.parser.package_data['small']['cost'], parcel.cost)
        self.assertEqual('small', parcel.package_type)

    def test_classify_parcel_small_in_lb(self):
        weight_factor = float(self.parser.conversion_scale['weight']['lb'])
        weight = float(self.parser.package_data['small']['weight']) / weight_factor
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['small']['height'])
        parcel = self.parser.calculate(length, breadth, height, weight, weight_unit='lb')

        self.assertEqual(self.parser.package_data['small']['cost'], parcel.cost)
        self.assertEqual('small', parcel.package_type)

    def test_classify_parcel_small_in_kg_overweight(self):
        weight_factor = float(self.parser.conversion_scale['weight']['kg'])
        weight = float(self.parser.package_data['small']['weight']) / weight_factor + 1
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['small']['height'])

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser.calculate(length, breadth, height, weight, weight_unit='kg')

    def test_classify_parcel_small_in_g_overweight(self):
        weight_factor = float(self.parser.conversion_scale['weight']['g'])
        weight = float(self.parser.package_data['small']['weight']) / weight_factor + 1
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['small']['height'])

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser.calculate(length, breadth, height, weight, weight_unit='g')

    def test_classify_parcel_small_in_lb_overweight(self):
        weight_factor = float(self.parser.conversion_scale['weight']['lb'])
        weight = float(self.parser.package_data['small']['weight']) / weight_factor + 1
        length = float(self.parser.package_data['small']['length'])
        breadth = float(self.parser.package_data['small']['breadth'])
        height = float(self.parser.package_data['small']['height'])

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser.calculate(length, breadth, height, weight, weight_unit='lb')

    """ Medium packages """

    def test_classify_parcel_medium_in_mm(self):
        size_factor = float(self.parser.conversion_scale['size']['mm'])
        length = float(self.parser.package_data['medium']['length']) / size_factor
        breadth = float(self.parser.package_data['medium']['breadth']) / size_factor
        height = float(self.parser.package_data['medium']['height']) / size_factor
        weight = float(self.parser.package_data['medium']['weight'])
        parcel = self.parser.calculate(length, breadth, height, weight, size_unit='mm')

        self.assertEqual(self.parser.package_data['medium']['cost'], parcel.cost)
        self.assertEqual('medium', parcel.package_type)

    def test_classify_parcel_medium_in_cm(self):
        size_factor = float(self.parser.conversion_scale['size']['cm'])
        length = float(self.parser.package_data['medium']['length']) / size_factor
        breadth = float(self.parser.package_data['medium']['breadth']) / size_factor
        height = float(self.parser.package_data['medium']['height']) / size_factor
        weight = float(self.parser.package_data['medium']['weight'])
        parcel = self.parser.calculate(length, breadth, height, weight, size_unit='cm')

        self.assertEqual(self.parser.package_data['medium']['cost'], parcel.cost)
        self.assertEqual('medium', parcel.package_type)

    def test_classify_parcel_medium_in_inch(self):
        size_factor = float(self.parser.conversion_scale['size']['inch'])
        length = float(self.parser.package_data['medium']['length']) / size_factor
        breadth = float(self.parser.package_data['medium']['breadth']) / size_factor
        height = float(self.parser.package_data['medium']['height']) / size_factor
        weight = float(self.parser.package_data['medium']['weight'])
        parcel = self.parser.calculate(length, breadth, height, weight, size_unit='inch')

        self.assertEqual(self.parser.package_data['medium']['cost'], parcel.cost)
        self.assertEqual('medium', parcel.package_type)

    def test_classify_parcel_medium_in_kg(self):
        weight_factor = float(self.parser.conversion_scale['weight']['kg'])
        weight = float(self.parser.package_data['medium']['weight']) / weight_factor
        length = float(self.parser.package_data['medium']['length'])
        breadth = float(self.parser.package_data['medium']['breadth'])
        height = float(self.parser.package_data['medium']['height'])
        parcel = self.parser.calculate(length, breadth, height, weight, weight_unit='kg')

        self.assertEqual(self.parser.package_data['medium']['cost'], parcel.cost)
        self.assertEqual('medium', parcel.package_type)

    def test_classify_parcel_medium_in_g(self):
        weight_factor = float(self.parser.conversion_scale['weight']['g'])
        weight = float(self.parser.package_data['medium']['weight']) / weight_factor
        length = float(self.parser.package_data['medium']['length'])
        breadth = float(self.parser.package_data['medium']['breadth'])
        height = float(self.parser.package_data['medium']['height'])
        parcel = self.parser.calculate(length, breadth, height, weight, weight_unit='g')

        self.assertEqual(self.parser.package_data['medium']['cost'], parcel.cost)
        self.assertEqual('medium', parcel.package_type)

    def test_classify_parcel_medium_in_lb(self):
        weight_factor = float(self.parser.conversion_scale['weight']['lb'])
        weight = float(self.parser.package_data['medium']['weight']) / weight_factor
        length = float(self.parser.package_data['medium']['length'])
        breadth = float(self.parser.package_data['medium']['breadth'])
        height = float(self.parser.package_data['medium']['height'])
        parcel = self.parser.calculate(length, breadth, height, weight, weight_unit='lb')

        self.assertEqual(self.parser.package_data['medium']['cost'], parcel.cost)
        self.assertEqual('medium', parcel.package_type)

    def test_classify_parcel_medium_in_kg_overweight(self):
        weight_factor = float(self.parser.conversion_scale['weight']['kg'])
        weight = float(self.parser.package_data['medium']['weight']) / weight_factor + 1
        length = float(self.parser.package_data['medium']['length'])
        breadth = float(self.parser.package_data['medium']['breadth'])
        height = float(self.parser.package_data['medium']['height'])

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser.calculate(length, breadth, height, weight, weight_unit='kg')

    def test_classify_parcel_medium_in_g_overweight(self):
        weight_factor = float(self.parser.conversion_scale['weight']['g'])
        weight = float(self.parser.package_data['medium']['weight']) / weight_factor + 1
        length = float(self.parser.package_data['medium']['length'])
        breadth = float(self.parser.package_data['medium']['breadth'])
        height = float(self.parser.package_data['medium']['height'])

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser.calculate(length, breadth, height, weight, weight_unit='g')

    def test_classify_parcel_medium_in_lb_overweight(self):
        weight_factor = float(self.parser.conversion_scale['weight']['lb'])
        weight = float(self.parser.package_data['medium']['weight']) / weight_factor + 1
        length = float(self.parser.package_data['medium']['length'])
        breadth = float(self.parser.package_data['medium']['breadth'])
        height = float(self.parser.package_data['medium']['height'])

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser.calculate(length, breadth, height, weight, weight_unit='lb')

    """ Large packages """

    def test_classify_parcel_large_in_mm(self):
        size_factor = float(self.parser.conversion_scale['size']['mm'])
        length = float(self.parser.package_data['large']['length']) / size_factor
        breadth = float(self.parser.package_data['large']['breadth']) / size_factor
        height = float(self.parser.package_data['large']['height']) / size_factor
        weight = float(self.parser.package_data['large']['weight'])
        parcel = self.parser.calculate(length, breadth, height, weight, size_unit='mm')

        self.assertEqual(self.parser.package_data['large']['cost'], parcel.cost)
        self.assertEqual('large', parcel.package_type)

    def test_classify_parcel_large_in_cm(self):
        size_factor = float(self.parser.conversion_scale['size']['cm'])
        length = float(self.parser.package_data['large']['length'] / size_factor)
        breadth = float(self.parser.package_data['large']['breadth'] / size_factor)
        height = float(self.parser.package_data['large']['height'] / size_factor)
        weight = float(self.parser.package_data['large']['weight'])
        parcel = self.parser.calculate(length, breadth, height, weight, size_unit='cm')

        self.assertEqual(self.parser.package_data['large']['cost'], parcel.cost)
        self.assertEqual('large', parcel.package_type)

    def test_classify_parcel_large_in_inch(self):
        size_factor = float(self.parser.conversion_scale['size']['inch'])
        length = float(self.parser.package_data['large']['length']) / size_factor
        breadth = float(self.parser.package_data['large']['breadth']) / size_factor
        height = float(self.parser.package_data['large']['height']) / size_factor
        weight = float(self.parser.package_data['large']['weight'])
        parcel = self.parser.calculate(length, breadth, height, weight, size_unit='inch')

        self.assertEqual(self.parser.package_data['large']['cost'], parcel.cost)
        self.assertEqual('large', parcel.package_type)

    def test_classify_parcel_large_in_kg(self):
        weight_factor = float(self.parser.conversion_scale['weight']['kg'])
        weight = float(self.parser.package_data['large']['weight']) / weight_factor
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])
        parcel = self.parser.calculate(length, breadth, height, weight, weight_unit='kg')

        self.assertEqual(self.parser.package_data['large']['cost'], parcel.cost)
        self.assertEqual('large', parcel.package_type)

    def test_classify_parcel_large_in_g(self):
        weight_factor = float(self.parser.conversion_scale['weight']['g'])
        weight = float(self.parser.package_data['large']['weight']) / weight_factor
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])
        parcel = self.parser.calculate(length, breadth, height, weight, weight_unit='g')

        self.assertEqual(self.parser.package_data['large']['cost'], parcel.cost)
        self.assertEqual('large', parcel.package_type)

    def test_classify_parcel_large_in_lb(self):
        weight_factor = float(self.parser.conversion_scale['weight']['lb'])
        weight = float(self.parser.package_data['large']['weight']) / weight_factor
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])
        parcel = self.parser.calculate(length, breadth, height, weight, weight_unit='lb')

        self.assertEqual(self.parser.package_data['large']['cost'], parcel.cost)
        self.assertEqual('large', parcel.package_type)

    def test_classify_parcel_large_in_kg_overweight(self):
        weight_factor = float(self.parser.conversion_scale['weight']['kg'])
        weight = float(self.parser.package_data['large']['weight']) / weight_factor + 1
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser.calculate(length, breadth, height, weight, weight_unit='kg')

    def test_classify_parcel_large_in_g_overweight(self):
        weight_factor = float(self.parser.conversion_scale['weight']['g'])
        weight = float(self.parser.package_data['large']['weight']) / weight_factor + 1
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser.calculate(length, breadth, height, weight, weight_unit='g')

    def test_classify_parcel_large_in_lb_overweight(self):
        weight_factor = float(self.parser.conversion_scale['weight']['lb'])
        weight = float(self.parser.package_data['large']['weight']) / weight_factor + 1
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])

        with self.assertRaisesRegex(parcel_parser.ParcelOverweightError, 'Parcel is overweight'):
            self.parser.calculate(length, breadth, height, weight, weight_unit='lb')

    """ Oversize packages """

    def test_classify_parcel_oversize_in_mm(self):
        size_factor = float(self.parser.conversion_scale['size']['mm'])
        length = float(self.parser.package_data['large']['length'] + 1 / size_factor)
        breadth = float(self.parser.package_data['large']['breadth'] / size_factor)
        height = float(self.parser.package_data['large']['height'] / size_factor)
        weight = float(self.parser.package_data['large']['weight'])

        with self.assertRaisesRegex(parcel_parser.ParcelOversizeError, 'Parcel length exceeded maximum limit'):
            self.parser.calculate(length, breadth, height, weight, size_unit='mm')

    def test_classify_parcel_oversize_in_cm(self):
        size_factor = float(self.parser.conversion_scale['size']['cm'])
        length = float(self.parser.package_data['large']['length'] + 1 / size_factor)
        breadth = float(self.parser.package_data['large']['breadth'] / size_factor)
        height = float(self.parser.package_data['large']['height'] / size_factor)
        weight = float(self.parser.package_data['large']['weight'])

        with self.assertRaisesRegex(parcel_parser.ParcelOversizeError, 'Parcel length exceeded maximum limit'):
            self.parser.calculate(length, breadth, height, weight, size_unit='cm')

    def test_classify_parcel_oversize_in_inch(self):
        size_factor = float(self.parser.conversion_scale['size']['inch'])
        length = float(self.parser.package_data['large']['length'] + 1 / size_factor)
        breadth = float(self.parser.package_data['large']['breadth'] / size_factor)
        height = float(self.parser.package_data['large']['height'] / size_factor)
        weight = float(self.parser.package_data['large']['weight'])

        with self.assertRaisesRegex(parcel_parser.ParcelOversizeError, 'Parcel length exceeded maximum limit'):
            self.parser.calculate(length, breadth, height, weight, size_unit='inch')

    """ Unsupported measurement units """

    def test_unsupported_size_unit(self):
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])
        weight = float(self.parser.package_data['large']['weight'])
        size_unit = 'km'

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError, 'Measurement unit not supported'):
            self.parser.calculate(length, breadth, height, weight, size_unit=size_unit)

    def test_invalid_size_unit(self):
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])
        weight = float(self.parser.package_data['large']['weight'])
        size_unit = 1

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError, 'Measurement unit not supported'):
            self.parser.calculate(length, breadth, height, weight, size_unit=size_unit)

    def test_unsupported_weight_unit(self):
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])
        weight = float(self.parser.package_data['large']['weight'])
        weight_unit = 'mg'

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError, 'Measurement unit not supported'):
            self.parser.calculate(length, breadth, height, weight, weight_unit=weight_unit)

    def test_invalid_weight_unit(self):
        length = float(self.parser.package_data['large']['length'])
        breadth = float(self.parser.package_data['large']['breadth'])
        height = float(self.parser.package_data['large']['height'])
        weight = float(self.parser.package_data['large']['weight'])
        weight_unit = 1

        with self.assertRaisesRegex(parcel_parser.InvalidConfigError, 'Measurement unit not supported'):
            self.parser.calculate(length, breadth, height, weight, weight_unit=weight_unit)


if __name__ == '__main__':
    unittest.main()
