#-*- coding: utf-8 -*-
from functools import reduce
def str2float(s):
	l=s.split('.')
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	return reduce(fn,map(char2num,l[0]+l[1]))/math.pow(10,len(l[1]))
print('str2float(\'123.456\')=',str2float('123.456'))