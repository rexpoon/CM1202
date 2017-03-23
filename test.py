from userdata import *

def lookuptutor():
	#from StackOverflow
	name=input("Enter name: ")

	for key, value in assignment.items():
		for v in value:
			if name in v:
				return key