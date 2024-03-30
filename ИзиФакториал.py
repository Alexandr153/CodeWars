import operator
from functools import reduce

number = list(range(1, 6))
print(reduce(operator.mul, number))