from tkinter import *
from tkinter.messagebox import *
import random

app = Tk()
# Message Window


def getstudents(filename):
    # Add code here
    import csv
    with open(filename) as csvfile:
        rdr = csv.DictReader(csvfile)
        Students=[row for row in rdr]
    return Students


def gettutors(filename):
    # Add code here
    import csv
    with open(filename) as csvfile:
        rdr = csv.DictReader(csvfile)
        Tutors=[row for row in rdr]
    return Tutors

def Assign(a,b):
    Tutors = gettutors(b)
    Students = getstudents(a)

    for tutor in Tutors:
        tutor['tutee'] = []
    for student in Students:
        student['assigned'] = False

    assignedStudentNumber = 0
    while (assignedStudentNumber<len(Students)):
        randomStudentIndex = random.randint(0, len(Students)-1)
        if (Students[randomStudentIndex]['assigned']==False):
            randomTutorIndex = random.randint(0, len(Tutors)-1)
            Tutors[randomTutorIndex]['tutee'].append( 
                Students[randomStudentIndex])
            Students[randomStudentIndex]['assigned'] = True
            assignedStudentNumber += 1


    return Tutors







def upload():
    get_data()


app.configure(bg='cornflower blue')

COLORS  =['blue', 'gold', 'cornflower blue']

#['Bob Smith', 'Prof Stuart Allen',
#'Alan Chan', 'Helen Philips']

# The position and size relative to the screen
app.geometry('500x500+450+140')

# The title of the program
app.title('Assign students to tutors')

# The icon
#app.wm_iconbitmap('MathIcon.ico')

# Object positioning in the program
# def GridPos:

# I might use the place() method for the screen layout.
Label(app, text="Please enter name of csv file.").place(x=150,y=80)
Label(app, text= "Students file:", bg="gold", fg="blue").place(x=120,y=120)
Label(app, text="Tutors file:", bg="gold", fg="blue").place(x=120,y=170)


def get_data():
    x_data = x.get()
    y_data = y.get()
    print ("x_data = {0} , y_data = {1} ".format(x_data,y_data))
    assignedTutors = Assign(x_data, y_data)
    print(assignedTutors)

x = Entry(app)
y = Entry(app)


x.place(x=220,y=120)
y.place(x=220,y=170)


# Buttons
B1 = Button(app,text='assign',bg='gold',fg='blue', command = upload ).place(x=210,y=220)

app.mainloop()











































































