"""
This file have a class
for use how interface.

"""

from tkinter import Tk, Frame, Label, StringVar, Text, Button, END, Menu
from utils.text_functions import converted_text
from utils.show_messages import notNotes, stopNotes, showAbout, noValidContent
from models.database import DataBase, db_path
from models.note import Note
from utils.colors import changeToBlue, changeToOrange, changeToRed, changeToYellow, changeToGreen
from utils.clear import clearInput

class UI:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Add Notes App.')
        self.wind.resizable(False, False)


        # frame conteiner
        frame = Frame(self.wind, height = 600, width = 1200)
        frame.pack(side = 'left')

        # title
        title = Label(frame, text = 'Notes.')
        title.grid(row = 0, column = 0, sticky = 'nesw', pady = 5, padx = 5)

        # other title
        Label(frame, text = 'Add a new Note.').grid(row = 1, column = 0, sticky = 'nesw', pady = 10, padx = 10)

        self.noteEntry = Text(frame, width = 20, height = 16)
        self.noteEntry.grid(row = 2, column = 0, sticky = 'nesw', pady = 5, padx = 5)

        # --------------- Buttons ------------------------
        saveButton = Button(frame, text = 'Add Note.', background = 'green')
        saveButton['command'] = self.addNote
        saveButton.grid(row = 3, column = 0, sticky = 'nesw', pady = 5, padx = 5)

        exitButton = Button(frame, text = 'Exit', background = 'red')
        exitButton['command'] = self.wind.destroy
        exitButton.grid(row = 4, column = 0, sticky = 'nesw', pady = 5, padx = 5)

        # Second Frame
        frame2 = Frame(self.wind, height = 600, width = 1200)
        frame2.pack()

        # ----------------- Labels for the Notes --------------------
        self.note1 = Label(frame2, text = '', width = 20, height = 5)
        self.note1.grid(row = 0, column = 0, sticky = 'nesw', pady = 5, padx = 5)

        self.note2 = Label(frame2, text = '', width = 20, height = 5)
        self.note2.grid(row = 0, column = 1, sticky = 'nesw', pady = 5, padx = 5)

        self.note3 = Label(frame2, text = '', width = 20, height = 5)
        self.note3.grid(row = 0, column = 2, sticky = 'nesw', pady = 5, padx = 5)

        self.note4 = Label(frame2, text = '', width = 20, height = 5)
        self.note4.grid(row = 0, column = 3, sticky = 'nesw', pady = 5, padx = 5)

        self.note5 = Label(frame2, text = '', width = 20, height = 5)
        self.note5.grid(row = 1, column = 0, sticky = 'nesw', pady = 5, padx = 5)

        self.note6 = Label(frame2, text = '', width = 20, height = 5)
        self.note6.grid(row = 1, column = 1, sticky = 'nesw', pady = 5, padx = 5)

        self.note7 = Label(frame2, text = '', width = 20, height = 5)
        self.note7.grid(row = 1, column = 2, sticky = 'nesw', pady = 5, padx = 5)

        self.note8 = Label(frame2, text = '', width = 20, height = 5)
        self.note8.grid(row = 1, column = 3, sticky = 'nesw', pady = 5, padx = 5)

        self.note9 = Label(frame2, text = '', width = 20, height = 5)
        self.note9.grid(row = 2, column = 0, sticky = 'nesw', pady = 5, padx = 5)

        self.note10 = Label(frame2, text = '', width = 20, height = 5)
        self.note10.grid(row = 2, column = 1, sticky = 'nesw', pady = 5, padx = 5)

        self.note11 = Label(frame2, text = '', width = 20, height = 5)
        self.note11.grid(row = 2, column = 2, sticky = 'nesw', pady = 5, padx = 5)

        self.note12 = Label(frame2, text = '', width = 20, height = 5)
        self.note12.grid(row = 2, column = 3, sticky = 'nesw', pady = 5, padx = 5)

        self.note13 = Label(frame2, text = '', width = 20, height = 5)
        self.note13.grid(row = 3, column = 0, sticky = 'nesw', pady = 5, padx = 5)

        self.note14 = Label(frame2, text = '', width = 20, height = 5)
        self.note14.grid(row = 3, column = 1, sticky = 'nesw', pady = 5, padx = 5)

        self.note15 = Label(frame2, text = '', width = 20, height = 5)
        self.note15.grid(row = 3, column = 2, sticky = 'nesw', pady = 5, padx = 5)

        self.note16 = Label(frame2, text = '', width = 20, height = 5)
        self.note16.grid(row = 3, column = 3, sticky = 'nesw', pady = 5, padx = 5)

        self.cards = [
            self.note1,
            self.note2,
            self.note3,
            self.note4,
            self.note5,
            self.note6,
            self.note7,
            self.note8,
            self.note9,
            self.note10,
            self.note11,
            self.note12,
            self.note13,
            self.note14,
            self.note15,
            self.note16
        ]

        # ------------- MENUS ----------------------
        barraMenu = Menu(self.wind)

        noteMenu = Menu(barraMenu, tearoff = 0)
        noteMenu.add_command(label = 'Add', command = self.addNote)
        noteMenu.add_command(label = 'Exit', command = self.wind.destroy)

        helpMenu = Menu(barraMenu, tearoff = 0)
        helpMenu.add_command(label = 'About', command = showAbout)

        # menu for change the cards's color
        backgroundsMenu = Menu(barraMenu, tearoff = 0)
        backgroundsMenu.add_command(label = 'Red', command = lambda : changeToRed(self.cards))
        backgroundsMenu.add_command(label = 'Blue', command = lambda : changeToBlue(self.cards))
        backgroundsMenu.add_command(label = 'Yellow', command = lambda : changeToYellow(self.cards))
        backgroundsMenu.add_command(label = 'Orange', command = lambda : changeToOrange(self.cards))
        backgroundsMenu.add_command(label = 'Green', command = lambda : changeToGreen(self.cards))

        barraMenu.add_cascade(menu = noteMenu, label = 'Note')
        barraMenu.add_cascade(menu = backgroundsMenu, label = 'Backgrounds')
        barraMenu.add_cascade(menu = helpMenu, label = 'Help')

        # esto tambien se puede hacer asi
        # self.wind.config(menu = barraMenu)
        self.wind['menu'] = barraMenu # es un poco menos verbosa jaja

        # variable for know if the notes view is full
        self.full = 0
        self.color_current = 'yellow'
        # showing the news notes
        self.showNotes()

    def __getNoteString(self):
        """
        Get the value of the note in the text
        input of the interface.
        """
        # getting
        val = self.noteEntry.get('1.0', END)
        return val

    def addNote(self):
        """
        Add the note at the database
        """

        # validating if the notes view is full
        if (self.full >= 16):
            # showing a window warning
            stopNotes()

        else:
            # getting the content of the note for form the query in the database
            content = self.__getNoteString()

            # validating if the content is empty for show a window
            if (content == '\n'):
                noValidContent()

            else:
                # creating a new note with this class
                note = Note(content)
                contentNote = note.content

                db = DataBase(db_path)
                # this is the query for save the note in the database
                query = f'INSERT INTO notes(content) VALUES(' + f'"{contentNote}"' + ')'
                db.insert(query)
                db.close()

                # showing the news notes
                self.showNotes()
                clearInput(self.noteEntry)

    def showNotes(self):
        db = DataBase(db_path)

        # validating if there notes for show it
        if (db.select('SELECT * FROM notes') == []):
            # showing a window of information
            notNotes()

            db.close()

        else:
            # recorriendo cada targeta y nota for show it in the interface
            for i in range(len(self.cards)):
                try:
                    # getting the content and converted
                    content = db.select('select content from notes')[i][0]
                    content = converted_text(content)

                    self.cards[i]['text'] = content
                    # changing the color of the labels
                    self.cards[i]['background'] = self.color_current
                    # adding the counter for validate
                    self.full += 1

                except IndexError:
                    pass

            # validating if is full the note view
            if (self.full >= 16):
                stopNotes()

            # closing the database
            db.close()
