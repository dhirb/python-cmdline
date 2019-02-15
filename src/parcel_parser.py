import yaml
from pathlib import Path
import os


class InvalidConfigError(Exception):
    """ Raised on IO error when reading config file, or when numeric fields contain non-numeric values """


class InvalidAttributeError(Exception):
    """ Raised when dimension or weight is non-numeric or non-positive """


class ParcelOverweightError(Exception):
    """ Raised when a parcel is overweight """


class ParcelOversizeError(Exception):
    """ Raised when a parcel is oversized """


class Parcel(object):
    """ Represents a parcel """

    length = 0
    breadth = 0
    height = 0
    weight = 0
    cost = -1
    package_type = 'NULL'

    def __init__(self, length, breadth, height, weight, cost, package_type):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.weight = weight
        self.cost = cost
        self.package_type = package_type


class Package(object):
    """ Represents the requirements of a shipping package """

    name = ''
    max_length = 0
    max_breadth = 0
    max_height = 0
    max_weight = 0
    cost = 0

    def __init__(self, name, length, breadth, height, weight, cost):
        self.name = name
        self.max_length = length
        self.max_breadth = breadth
        self.max_height = height
        self.max_weight = weight
        self.cost = cost


class ParcelParser:
    """ Parser to classify the shipping package needed to ship a parcel """

    def __init__(self):
        self.packages = []
        self.package_data = {}
        self.conversion_scale = {}

        try:
            project_root = Path(__file__).parent.parent

            self._get_package_data(project_root)
            self._setup_packages(self.package_data)

            self._setup_conversion_scale(project_root)
        except FileNotFoundError:
            raise InvalidConfigError('Error: Config file is missing')
        except IOError:
            raise InvalidConfigError('Error: Failed to read config file')

    def _get_package_data(self, project_root):
        """
        Get package data from config file.

        :param project_root: Path to project root.
        :return: Nothing.
        """

        with open(os.path.join(project_root, 'config/packages.yaml'), 'r') as package_data:
            self.package_data = yaml.safe_load(package_data)

        if not self.package_data:
            raise InvalidConfigError('Error: Package config file is empty')

    def _setup_packages(self, package_data):
        """
        Set up the requirements of each shipping packages.

        :param package_data: Raw package data from config file.
        :return: Nothing.
        """

        try:
            for key in package_data:
                package = Package(key,
                                  self._validate_numeric(package_data[key]['length'], 'length'),
                                  self._validate_numeric(package_data[key]['breadth'], 'breadth'),
                                  self._validate_numeric(package_data[key]['height'], 'height'),
                                  self._validate_numeric(package_data[key]['weight'], 'weight'),
                                  self._validate_numeric(package_data[key]['cost'], 'cost'))
                self.packages.append(package)
        except KeyError as e:
            raise InvalidConfigError('Error: Missing {} key in packages config file'.format(e))

        # Sort packages based on ascending dimension
        self.packages = sorted(self.packages, key=lambda p: (p.max_length, p.max_breadth, p.max_height))

    def _setup_conversion_scale(self, project_root):
        """
        Get conversion scheme from config.

        :param project_root: Path to project root.
        :return: Nothing.
        """

        with open(os.path.join(project_root, 'config/conversion.yaml'), 'r') as conversion_scale:
            self.conversion_scale = yaml.safe_load(conversion_scale)

        # Sanity check
        if not self.conversion_scale:
            raise InvalidConfigError('Error: Conversion config file is empty')

    def _setup_conversion_factors(self, size_unit, weight_unit):
        """
        Set up multiplicative factors for different measurement unit.

        :param size_unit: Dimension measurement unit.
        :param weight_unit: Weight measurement unit.
        :return: Nothing.
        """

        try:
            self.size_factor = float(self.conversion_scale['size'][str(size_unit).strip().lower()])
            if self.size_factor <= 0:
                raise InvalidConfigError('Dimension size factor must be positive')

            self.weight_factor = float(self.conversion_scale['weight'][str(weight_unit).strip().lower()])
            if self.weight_factor <= 0:
                raise InvalidConfigError('Weight factor must be positive')

        except KeyError:
            raise InvalidConfigError('Measurement unit not supported')
        except ValueError:
            raise InvalidConfigError('Error: Conversion config file contains invalid numeric parameter')
        except OverflowError:
            raise InvalidConfigError('Error: Config field value must be within numerical limit')

    @staticmethod
    def _validate_numeric(x, name):
        """
        Helper method to check if the given param is a number.

        :param x: Param to validate.
        :param name: Canonical name of the param.
        :return: Given param in numeric form.
        """

        try:
            x = float(x)
            if x <= 0:
                raise InvalidAttributeError('Error: {} must be positive'.format(str(name)))

            return x
        except ValueError:
            raise InvalidAttributeError('Error: {} must be numeric'.format(str(name)))
        except OverflowError:
            raise InvalidAttributeError('Error: {} must be within numerical limit'.format(str(name)))

    def _classify_parcel(self, length, breadth, height, weight):
        """
        Determine the shipping cost and package type of the given parcel.

        :param length: Parcel length.
        :param breadth: Parcel breadth.
        :param height: Parcel height.
        :param weight: Parcel weight.
        :return: Parcel object with shipping cost and package type computed.
        """

        # Since self.packages is sorted in ascending order, the dimension limits can be found in the last element
        if length > self.packages[-1].max_length:
            raise ParcelOversizeError('Parcel length exceeded maximum limit')
        if breadth > self.packages[-1].max_breadth:
            raise ParcelOversizeError('Parcel breadth exceeded maximum limit')
        if height > self.packages[-1].max_height:
            raise ParcelOversizeError('Parcel height exceeded maximum limit')

        # Check each available shipping packages and determine if the parcel fits the requirements
        for package in self.packages:
            if length <= package.max_length and breadth <= package.max_breadth and \
                    height <= package.max_height and weight <= package.max_weight:
                return Parcel(length, breadth, height, weight, package.cost, package.name)

        # At this point, the parcel must be overweight
        raise ParcelOverweightError('Parcel is overweight')

    def calculate(self, length, breadth, height, weight, size_unit='mm', weight_unit='kg'):
        """
        Calculates the shipping cost and package type of a parcel with given dimension and weight.

        :param length: Length of the parcel.
        :param breadth: Breadth of the parcel.
        :param height: Height of the parcel.
        :param weight: Weight of the parcel.
        :param size_unit: Measurement unit for dimension. Defaults to mm.
        :param weight_unit: Measurement unit for weight. Defaults to kg.
        :return: Parcel with shipping cost and package type computed.
        """

        # Setup size and weight conversion factors
        self._setup_conversion_factors(size_unit, weight_unit)

        # Calculate dimension and weight with multiplicative factors
        adjusted_length = self.size_factor * self._validate_numeric(length, 'length')
        adjusted_breadth = self.size_factor * self._validate_numeric(breadth, 'breadth')
        adjusted_height = self.size_factor * self._validate_numeric(height, 'height')
        adjusted_weight = self.weight_factor * self._validate_numeric(weight, 'weight')

        return self._classify_parcel(adjusted_length, adjusted_breadth, adjusted_height, adjusted_weight)
