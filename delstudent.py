from tkinter import *
from tkinter.messagebox import *
import random



from userdata import *



app = Tk()
# Message Window


def messagePop():

	get_data()

	name=x.get()
	for key, value in assignment.items():
		for v in value:
			if name in v:
				messagebox.showinfo("ddddd",v+" has been deleted from the group of tutor: "+key)





app.configure(bg='cornflower blue')

COLORS  =['blue', 'gold', 'cornflower blue']

# The position and size relative to the screen
app.geometry('500x500+450+140')

# The title of the program
app.title('Search tutor for individual student')


# Object positioning in the program
Label(app, text="Please enter the first and last name of student.").place(x=10,y=0)
Label(app, text= "Full Name:", bg="gold", fg="blue").place(x=10,y=120)


# Entry
def get_data():
    x_data = x.get()
    print ("x_data = {0}".format(x_data))

x = Entry(app)



x.place(x=90,y=120)


# Buttons
B1 = Button(app,text='Search',bg='gold',fg='blue', command = messagePop).place(x=425,y=450)

app.mainloop()