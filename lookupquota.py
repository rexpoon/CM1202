#C1670764

from collections import Counter
from userdata import *
from tkinter import *
from tkinter.messagebox import *

app = Tk()
label=Label(app,text="Tutor Name,Assigned group, Assigned tutees, Assigned quota, Available quota")
box = Listbox(app, width=50)


def lookupquota():
	dictionary = assignment		#can customise the  
	i = 0
	for item in dictionary:
		assigned= len(dictionary[item])
		for key in tutorlist:
			if item == key:
				tuteeclass = tutorlist[key]
		if tuteeclass == 0:
			quota = UGquota
			group = "UG"
		elif tuteeclass == 1:
			quota = PGquota
			group = "PG"
		else:
			raise Exception("The quota of a tutor has not been specified. Please check the userdata.")
		available= (quota-assigned)
		exportlist=[item, group, assigned, quota, available]	#can customise the output
		box.insert(i,exportlist)
		i += 1

app.title('Quotas of tutees of every staff member')
app.geometry('500x500+450+140')
app.configure(bg='cornflower blue')

label.pack()
box.pack(command=lookupquota())





app.mainloop()