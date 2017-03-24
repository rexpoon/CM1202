#C1670764

from collections import Counter
from userdata import *
from tkinter import *
from tkinter.messagebox import *

app = Tk()
box = Listbox(app, width=75)
box.insert(0,"Tutor Name, Assigned tutees, Assigned quota, Available quota")

def lookupquota():
	dictionary = assignment
	i = 1
	for item in dictionary:
		assigned= len(dictionary[item])
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
		exportlist=[item, assigned, quota, available]
		box.insert(i,exportlist)
		i += 1

app.title('Quotas of tutees of every staff member')
app.geometry('500x500+450+140')
app.configure(bg='cornflower blue')
box.pack(command=lookupquota())





app.mainloop()