#C1670764

from collections import Counter
from userdata import *


def lookupquota(dictionary):
	for item in dictionary:
		assigned= len(dictionary[item])
		print("Tutees assigned to "+item+": "+str(assigned))
		available= (UGquota-assigned)
		print("Available quotas for "+item+": "+str(available))
	pass