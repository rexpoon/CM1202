from tkinter import *
from tkinter.messagebox import *
import random



from userdata1 import *



app = Tk()
# Message Window
AliaIAbdelmoty = assignment["Alia I Abdelmoty"]
MartinCaminada = assignment["Martin Caminada"]
MatthewJohn = assignment["Matthew John"]



def messagePop():
	global MartinCaminada
	get_data()

	name=x.get()
	for key, value in assignment.items():
		for v in value:
			if name in v:
				messagebox.showinfo("Delete Student",v+" has been deleted from the group of tutor: "+key+". "+v+" has been re-assign to the group of tutor: "+z.get())
			
			if v == "Alex Cheung":
				del MartinCaminada[1]
				print (MartinCaminada)





	assignment[z.get()].append(name)
	print (assignment[z.get()])



app.configure(bg='cornflower blue')

COLORS  =['blue', 'gold', 'cornflower blue']

# The position and size relative to the screen
app.geometry('500x500+450+140')

# The title of the program
app.title('Delete a student from the tutor list')


# Object positioning in the program
Label(app, text="Please enter the full name of student.").place(x=10,y=0)
Label(app, text="Full Name:", bg="gold", fg="blue").place(x=10,y=120)
Label(app, text="alternative tutor:", bg="gold", fg="blue").place(x=10,y=220)

# Entry
def get_data():
    x_data = x.get()
    z_data = z.get()
x = Entry(app)
z = Entry(app)


x.place(x=90,y=120)
z.place(x=120,y=220)


# Buttons
B1 = Button(app,text='Submit',bg='gold',fg='blue', command = messagePop).place(x=425,y=450)

app.mainloop()