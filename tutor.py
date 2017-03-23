from tkinter import *
from tkinter.messagebox import *
#import userdata
from userdata import *


app = Tk()
# Message Window

def messagePop():

    get_data()

    for item in assignment:
        if item.find("Zachariah Butler"):
            messagebox.showinfo("Result", "Alia I Abdelmoty")
        elif item.find("Samuel East"):
            messagebox.showinfo("Result", "Martin Caminada")
        elif item.find("Robin Watson"):
            messagebox.showinfo("Result", "Matthew John")
        elif item.find("Joshua Davies"):
            messagebox.showinfo("Result", "Alia I Abdelmoty")
        elif item.find("Samuel Healey"):
            messagebox.showinfo("Result", "Alia I Abdelmoty")
        elif item.find("Ahamed Abdul Kayee"):
            messagebox.showinfo("Result", "Martin Caminada")
        elif item.find("Alex Cheung"):
            messagebox.showinfo("Result", "Martin Caminada")
        elif item.find("Charlie Bennett"):
            messagebox.showinfo("Result", "Matthew John")
        elif item.find("Kieran Fewell"):
            messagebox.showinfo("Result", "Matthew John")
        elif item.find("Joshua Wong"):
            messagebox.showinfo("Result", "Matthew John")
        elif item.find("Mia Davis"):
            messagebox.showinfo("Result", "Yukun Lai")
        elif item.find("Lloyd Francis"):
            messagebox.showinfo("Result", "Yukun Lai")
        elif item.find("Nicole Kan"):
            messagebox.showinfo("Result", "Yukun Lai")
        elif item.find("Zachary Allen"):
            messagebox.showinfo("Result", "Kirill Sidorov")
        elif item.find("Giorgos Andreou"):
            messagebox.showinfo("Result", "Kirill Sidorov")
        elif item.find("Max Milburn"):
            messagebox.showinfo("Result", "Kirill Sidorov")

app.configure(bg='cornflower blue')

COLORS  =['blue', 'gold', 'cornflower blue']

# The position and size relative to the screen
app.geometry('500x500+450+140')

# The title of the program
app.title('Search tutor for individual student')


# Object positioning in the program
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
B1 = Button(app,text='Search',bg='gold',fg='blue', command = messagePop).place(x=425,y=450)

app.mainloop()

