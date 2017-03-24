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
				messagebox.showinfo("Delete Student",v+" has been deleted from the group of tutor: "+key)





app.configure(bg='cornflower blue')

COLORS  =['blue', 'gold', 'cornflower blue']

# The position and size relative to the screen
app.geometry('500x500+450+140')

# The title of the program
app.title('Delete a student from the tutor list')


# Object positioning in the program
Label(app, text="Please enter the first and last name of student.").place(x=10,y=0)
Label(app, text="First Name:", bg="gold", fg="blue").place(x=10,y=120)
Label(app, text="Last Name:", bg="gold", fg="blue").place(x=10,y=170)
Label(app, text="alternative tutor:", bg="gold", fg="blue").place(x=10,y=220)

# Entry
def get_data():
    x_data = x.get()
    y_data = y.get()
    print ("x_data = {0} , y_data = {1} ".format(x_data,y_data))

x = Entry(app)
y = Entry(app)


x.place(x=90,y=120)
y.place(x=90,y=170)



# Buttons
B1 = Button(app,text='Search',bg='gold',fg='blue', command = messagePop).place(x=425,y=450)

app.mainloop()