# Main Package  File -- Very Important

# this line import the calculate function from the calculator.py module

from .calculate import calculate

# There line going to import the basic add subtract functions from the basic __init__.py module

from ..basic import add, subtract

# this line is going to import the multiply and divide functions from the basic __init__.py module

from ..advance import multiply, divide
