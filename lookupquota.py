#C1670764

from collections import Counter
from userdata import *
from tkinter import *
from tkinter.messagebox import *

app = Tk()

def lookupquota():
	dictionary = assignment
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

app.geometry('500x500+450+140')

Label(app, text='Tutor name').grid(row=0,column=1, sticky=W)
Label(app, text='Number of tutees').grid(row=0, column=2, sticky=W)
Label(app, text='Tutees quota').grid(row=0,column=3, sticky=W)
Label(app, text='Available quota').grid(row=0,column=4, sticky=W)


app.mainloop()