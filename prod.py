#-*- coding: utf-8 -*-
from functools import reduce
def prod(L):
	def product_rule(x,y):
		return x*y
	return reduce(product_rule,L)
print ('3*5*7*9=', prod([3,5,7,9]))