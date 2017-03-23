#C1670764

from collections import Counter
from userdata import *
from tkinter import *
from tkinter.messagebox import *

def lookupquota(dictionary):
	for item in dictionary:
		assigned= len(dictionary[item])
		print("Tutees assigned to "+item+": "+str(assigned))
		for key in tutorlist:
			if item == key:
				tuteeclass = tutorlist[key]
			if tuteeclass == 0:
				quota = UGquota
			elif tuteeclass == 1:
				quota = PGquota
			else:
				raise Exception("The quota of a tutor has not been specified. Please check the userdata.")

		available= (quota-assigned)
		print(item+" has a quota of "+str(quota)+" tutees.")
		print("Available quotas for "+item+": "+str(available))
	pass