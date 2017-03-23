"""
>>>lookupquota(assignment,4)
Tutees assigned to Jack: 3
Available quotas for Jack: 1
Tutees assigned to 
"""
#C1670764
from collections import Counter

assignment = {"Jack":["Simon Hui","Ivan Shum","Rex Poon"],"Matt":["William Cooter","Ameilia Huggons","Zifan Zhao","Sophie Coverdale"]}


def lookupquota(dictionary,quota):
	for item in dictionary:
		assigned= len(dictionary[item])
		print("Tutees assigned to "+item+": "+str(assigned))
		available= (quota-assigned)
		print("Available quotas for "+item+": "+str(available))
	pass