"""
>>>lookupquota(assignment,4)
Tutees assigned to Jack: 3
Available quotas for Jack: 1
Tutees assigned to Matt: 4
Available quotas for Matt: 0
"""
#C1670764
from collections import Counter
import system

def lookupquota(dictionary,quota):
	for item in dictionary:
		assigned= len(dictionary[item])
		print("Tutees assigned to "+item+": "+str(assigned))
		available= (quota-assigned)
		print("Available quotas for "+item+": "+str(available))
	pass