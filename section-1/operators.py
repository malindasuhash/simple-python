print(10 / 3) # Prints 3.3333
print(10 // 3) # Prints 3 truncates the remainder
print(10.0 / 3.0) # Prints 3.33333
print(10.0 // 3.0) # Prints 3.0 Take a note of the decimal place
print(10 / 3.0 ) # Prints 3.33333
print(10 // 3.0) # Prints 3.0; note the truncation but decimal place
print(10.0 / 3) # Prints 3.33333
print(10.0 // 3) # Prints 3.0; note the truncation and decimal place

# // is an integer division operator

def square(x):
    return x * x

def sub(x, y):
    return x - y

print(square(10))

print(square)

# Note the triple quotes 
print("""Oh no, she said "broken" """)

print(10,400) # Sees this as two numbers
print(10400) # Single number
print("""This text 
is multi-line""") # Multi-line text approach

# Converters - helps to convert from one type to another
print(int(3.43)) # Prints 3 by truncating decimal places
# print(int("3.23")) This errors out because string cannot be converted to a decimal in single go.
# One would expect the string to be converted to 3 truncating .23.
# However int(3.43) would successfully convert because to the conversion
# from one to the other type happens in the single step.

# Methods in question are: str, int, float
print(str(1234)) # prints the string version of value 1234
print(int(3.45)) # prints 3 by truncating decimal places
print(float(2)) # prints 2.0 by converting to a float that include decimals.

# Removal of decimal places as a result of conversions is called
# "truncation towards zero" in the number line

# Variables - case sensitive, must start with a letter or underscore 
# Note that reserved words are not allowed
# Python thought process - variables do not have a type but values does
# which means a variable during its lifetime can point of values of different
# types.

x = 5
print(x)

x = 10
print(x)

_x = 20
print(_x)
