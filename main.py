from src import parcel_parser
import sys


def get_measurement_unit(units, message):
    """
    Prompt user for measurement unit to use when calculating shipping package.

    :param units: Available measurement units.
    :param message: Prompt message.
    :return: Measurement unit selected by the user.
    """

    while True:
        unit = str(input(message)).strip().lower()

        if unit not in units:
            print('Invalid measurement unit\n')
        else:
            return unit


def get_numeric(message):
    """
    Prompt user for a parcel attribute.

    :param message: Prompt message.
    :return: Parcel attribute.
    """

    while True:
        try:
            return float(input(message))
        except ValueError:
            print('Value must be numeric\n')
        except OverflowError:
            print('Value exceeded numerical limit\n')


def main():
    """
    Entry point of the program.
    :return: Nothing.
    """

    # Setup
    try:
        parser = parcel_parser.ParcelParser()
    except parcel_parser.InvalidConfigError as ex:
        print(ex)
        sys.exit(1)

    print('Welcome to TradeMe parcel shipping service.\n\n')

    try:
        size_units = ['cm', 'mm', 'inch']
        size_unit = get_measurement_unit(size_units, 'Enter dimension unit ({}): '.format(', '.join(size_units)))
        length = get_numeric('Enter parcel length: ')
        breadth = get_numeric('Enter parcel breadth: ')
        height = get_numeric('Enter parcel height: ')

        weight_units = ['kg', 'g', 'lb']
        weight_unit = get_measurement_unit(weight_units, 'Enter weight unit ({}): '.format(', '.join(weight_units)))
        weight = get_numeric('Enter parcel weight: ')

        parcel = parser.calculate(length, breadth, height, weight, size_unit=size_unit, weight_unit=weight_unit)

        print('\n\nPackaging solution found!\n')
        print('Package type: {}'.format(parcel.package_type.capitalize()))
        print('Shipping cost: ${:1,.2f}'.format(parcel.cost))

    except (parcel_parser.ParcelOversizeError, parcel_parser.ParcelOverweightError) as e:
        print('\n\nNo packaging solution: {}'.format(e))

    except parcel_parser.InvalidAttributeError as e:
        print('\n\n{}'.format(e))
        sys.exit(1)


if __name__ == '__main__':
    main()
