from userdata import *

def lookuptutor(name):
	#from StackOverflow
	for key, value in assignment.items():
		for v in value:
			if name in v:
				return key