## Introduction ##

This is my submission to a coding exercise. In this project I demonstrated how a simple command line program can be 
written in Python and tested with automated unit tests.

## Project requirements ##

We're looking to make selling items even easier and so we've decided to build our very own package shipping network. We've dug a tunnel between the North and South Islands that enables us to offer the same rates for parcels sent anywhere in the country, and we've just finished fueling up our fleet of courier vans; all that remains to be done is to update the website so that users can be advised how much their items will cost to send.

Our new service shipping costs are based on size and we offer different prices for small, medium, and large boxes. Unfortunately we're currently unable to move heavy packages so we've placed an upper limit of 25kg per package.

| Package Type | Length | Breadth | Height | Cost |
| ------------ | ------ | ------- | ------ | ---- |
| Small | 200mm | 300mm | 150mm | $5.00 |
| Medium | 300mm | 400mm | 200mm| $7.50 |
| Large | 400mm | 600mm | 250mm | $8.50 |

Implement a component that, when supplied the dimensions (length x breadth x height) and weight of a package, can advise on the cost and type of package required. If the package exceeds these dimensions - or is over 25kg - then the service should not return a packaging solution.

## Solution Overview ##

We create a parcel parser to classify the package type for each parcel, given its dimension and weight.

In ```src/parcel_parser.py```, we expose a public interface ```calculate()```. It consumes the dimension and weight of 
a parcel, and returns a ```Parcel``` object that contains the package type and shipping cost required to ship this 
parcel.
```
calculate(length, breadth, height, weight, size_unit='mm', weight_unit='kg')
```
Optionally, we can set the measurement units for dimension and weight. List of supported units and their respective 
multiplicative factors can be found and added in ```config/conversion.yaml```. Defaults are mm for dimension and kg for 
weight.

## Prerequisite ##

1. Install Python 3. Instructions available [here](https://docs.python-guide.org/starting/installation/).
2. If pip is not installed, see [here](https://pip.pypa.io/en/stable/installing/).
3. Install dependencies.
```
pip install -r requirements.txt
```

## Usage ##
### Command line ###

This will initiate an interactive command line program.
```
python main.py
```

## Unit test ##

To run all unit tests on ```ParcelParser```:
```
python -m unittest
```

For verbosity on each test cases:
```
python -m unittest -v
```

To run individual test file:
```
python -m unittest tests/<test_case>.py
```

## Improvements ##
### Shipping package customisation ###

In this solution, the packaging solution requirements are extracted to a config file (*see 
```config/packages.yaml```*). This approach allows us to add new packaging types or modify existing packages without 
having to modify the code. In addition, we can outsource this task to any staff as long as the strict YAML format is 
adhered. Doing so will not only alleviate the burden on engineering, but also minimise the risk of miscommunication.

Furthermore, while the project requirement states that the parcel weight limit of 25kg is the same across all package 
types, this solution is implemented such that each package types has their own weight limit (in this case, they are all 
set to 25kg). Doing so allows us to easily modify the weight limits without code changes.

### Measurement unit conversion ###

Often, as part of I18N, we will need to convert dimensions and weights for different locales that use different 
measurement units. Again, the multiplicative factors are extracted to a config file (*see 
```config/conversion.yaml```*), with millimeter set as the default unit for parcel dimension and kilogram for weight.

## Considered but not done ##
### Database ###

For simplicity, config files were used in this solution rather than a database approach. Ideally, we would like our 
data to reside in a database instead of arbitrary files.

### RESTful implementation ###

Again, for reducing complexity. However, we can easily convert the input and output of ```calculate()``` to JSON for 
immediate REST support.

## Version tested ##

Python 3.7.0
