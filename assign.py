from tkinter import *
from tkinter.messagebox import *
import random

app = Tk()



def getstudents(filename):
    import csv
    with open(filename) as csvfile:
        rdr = csv.DictReader(csvfile)
        Students=[row for row in rdr]
    return Students


def gettutors(filename):
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


def assign():
    get_data()


app.configure(bg='cornflower blue')

COLORS  =['blue', 'gold', 'cornflower blue']

app.geometry('500x500+450+140')

app.title('Assign students to tutors')

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

B1 = Button(app,text='Assign students to tutors',bg='gold',fg='blue', command = assign ).place(x=170,y=220)

app.mainloop()











































































