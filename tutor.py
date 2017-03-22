from tkinter import *
from tkinter.messagebox import *

app = Tk()
# Message Window

def messagePop():

    tutor = ['Bob Smith', 'Prof Stuart Allen', 'Alan Chan', 'Helen Philips', 'Martha Milton', 'Matt Morgan']

    get_data()

    if tutor[0]:
        messagebox.showinfo('Result', tutor[1])

    elif tutor[2]:
        messagebox.showinfo('Result', tutor[3])

    elif tutor[4]:
        messagebox.showinfo('Result', tutor[5])
    #messagebox.showinfo('Result', tutor)
    

# Background colour

app.configure(bg='cornflower blue')

COLORS  =['blue', 'gold', 'cornflower blue']

#['Bob Smith', 'Prof Stuart Allen',
#'Alan Chan', 'Helen Philips']

# The position and size relative to the screen
app.geometry('500x500+450+140')

# The title of the program
app.title('Search tutor for individual student')

# The icon
app.wm_iconbitmap('MathIcon.ico')

# Object positioning in the program
# def GridPos:

# I might use the place() method for the screen layout.
Label(app, text="Please enter the first and last name of student.").place(x=10,y=0)
Label(app, text= "First Name:", bg="gold", fg="blue").place(x=10,y=120)
Label(app, text="Last Name:", bg="gold", fg="blue").place(x=10,y=170)

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
B1 = Button(app,text='Search',bg='gold',fg='blue', command = messagePop ).place(x=425,y=450)

app.mainloop()
