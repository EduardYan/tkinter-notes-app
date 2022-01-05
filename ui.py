"""
This file have a class
for use how interface.

"""

from tkinter import Frame, Label, Text, Button, END, Menu
from models.database import DataBase, db_path
from models.note import Note
from colors.colors import changeToBlue, changeToOrange, changeToRed, changeToYellow, changeToGreen
from messages.show_messages import notNotes, stopNotes, showAbout, noValidContent
from utils.text_functions import converted_text
from utils.clear import clearInput

class UI:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Add Notes App.')
        # self.wind.resizable(False, False)
        self.wind['background'] = '#ffb'


        # frame conteiner
        frame = Frame(self.wind, height = 600, width = 1200)
        frame['background'] = '#ffb'
        frame.pack(side = 'left')

        # title
        title = Label(frame, text = 'Notes.')
        title['background'] = '#ffb'
        title['foreground'] = '#333'
        title.grid(row = 0, column = 0, sticky = 'nesw', pady = 10, padx = 5)

        # other title
        Label(frame, text = 'Add a new Note.', background = '#ffb').grid(row = 1, column = 0, sticky = 'nesw', pady = 10, padx = 10)

        self.noteEntry = Text(frame, width = 20, height = 16, font = 'sans-serif')
        self.noteEntry.grid(row = 2, column = 0, sticky = 'nesw', pady = 5, padx = 5)

        # --------------- Buttons ------------------------
        saveButton = Button(frame, text = 'Add Note.', background = '#cfc')
        saveButton['command'] = self.addNote
        saveButton['cursor'] = 'hand2'
        saveButton['activebackground'] = '#afa'
        saveButton.grid(row = 3, column = 0, sticky = 'nesw', pady = 5, padx = 5)

        exitButton = Button(frame, text = 'Exit', background = '#fbb')
        exitButton['command'] = self.wind.destroy
        exitButton['cursor'] = 'hand2'
        exitButton['activebackground'] = '#faa'
        exitButton.grid(row = 4, column = 0, sticky = 'nesw', pady = 5, padx = 5)

        # Second Frame
        frame2 = Frame(self.wind, height = 600, width = 1200)
        frame2['background'] = '#ffb'
        frame2.pack()

        # ----------------- Labels for the Notes --------------------
        self.note1 = Label(frame2, text = '', width = 20, height = 5)
        self.note1['background'] = '#ffb'
        self.note1.grid(row = 0, column = 0, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton = Button(self.note1, text = 'Delete')
        # deleteButton['background'] = '#fbb'
        # deleteButton['cursor'] = 'hand2'
        # deleteButton['activebackground'] = '#faa'
        # deleteButton.pack(side = 'bottom', fill = 'x')

        self.note2 = Label(frame2, text = '', width = 20, height = 5)
        self.note2['background'] = '#ffb'
        self.note2.grid(row = 0, column = 1, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton2 = Button(self.note2, text = 'Delete')
        # deleteButton2['background'] = '#fbb'
        # deleteButton2['cursor'] = 'hand2'
        # deleteButton2['activebackground'] = '#faa'
        # deleteButton2.pack(side = 'bottom', fill = 'x')

        self.note3 = Label(frame2, text = '', width = 20, height = 5)
        self.note3['background'] = '#ffb'
        self.note3.grid(row = 0, column = 2, sticky = 'nesw', pady = 5, padx = 5)
        deleteButton3 = Button(self.note3, text = 'Delete')
        # deleteButton3['background'] = '#fbb'
        # deleteButton3['cursor'] = 'hand2'
        # deleteButton3['activebackground'] = '#faa'
        # deleteButton3.pack(side = 'bottom', fill = 'x')

        self.note4 = Label(frame2, text = '', width = 20, height = 5)
        self.note4['background'] = '#ffb'
        self.note4.grid(row = 0, column = 3, sticky = 'nesw', pady = 5, padx = 5)
        deleteButton4 = Button(self.note4, text = 'Delete')
        # deleteButton4['background'] = '#fbb'
        # deleteButton4['cursor'] = 'hand2'
        # deleteButton4['activebackground'] = '#faa'
        # deleteButton4.pack(side = 'bottom', fill = 'x')

        self.note5 = Label(frame2, text = '', width = 20, height = 5)
        self.note5['background'] = '#ffb'
        self.note5.grid(row = 1, column = 0, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton5 = Button(self.note5, text = 'Delete')
        # deleteButton5['background'] = '#fbb'
        # deleteButton5['cursor'] = 'hand2'
        # deleteButton5['activebackground'] = '#faa'
        # deleteButton5.pack(side = 'bottom', fill = 'x')

        self.note6 = Label(frame2, text = '', width = 20, height = 5)
        self.note6['background'] = '#ffb'
        self.note6.grid(row = 1, column = 1, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton6 = Button(self.note6, text = 'Delete')
        # deleteButton6['background'] = '#fbb'
        # deleteButton6['cursor'] = 'hand2'
        # deleteButton6['activebackground'] = '#faa'
        # deleteButton6.pack(side = 'bottom', fill = 'x')

        self.note7 = Label(frame2, text = '', width = 20, height = 5)
        self.note7['background'] = '#ffb'
        self.note7.grid(row = 1, column = 2, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton7 = Button(self.note7, text = 'Delete')
        # deleteButton7['background'] = '#fbb'
        # deleteButton7['cursor'] = 'hand2'
        # deleteButton7['activebackground'] = '#faa'
        # deleteButton7.pack(side = 'bottom', fill = 'x')

        self.note8 = Label(frame2, text = '', width = 20, height = 5)
        self.note8['background'] = '#ffb'
        self.note8.grid(row = 1, column = 3, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton8 = Button(self.note8, text = 'Delete')
        # deleteButton8['background'] = '#fbb'
        # deleteButton8['cursor'] = 'hand2'
        # deleteButton8['activebackground'] = '#faa'
        # deleteButton8.pack(side = 'bottom', fill = 'x')

        self.note9 = Label(frame2, text = '', width = 20, height = 5)
        self.note9['background'] = '#ffb'
        self.note9.grid(row = 2, column = 0, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton9 = Button(self.note9, text = 'Delete')
        # deleteButton9['background'] = '#fbb'
        # deleteButton9['cursor'] = 'hand2'
        # deleteButton9['activebackground'] = '#faa'
        # deleteButton9.pack(side = 'bottom', fill = 'x')


        self.note10 = Label(frame2, text = '', width = 20, height = 5)
        self.note10['background'] = '#ffb'
        self.note10.grid(row = 2, column = 1, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton10 = Button(self.note10, text = 'Delete')
        # deleteButton10['background'] = '#fbb'
        # deleteButton10['cursor'] = 'hand2'
        # deleteButton10['activebackground'] = '#faa'
        # deleteButton10.pack(side = 'bottom', fill = 'x')

        self.note11 = Label(frame2, text = '', width = 20, height = 5)
        self.note11['background'] = '#ffb'
        self.note11.grid(row = 2, column = 2, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton11 = Button(self.note11, text = 'Delete')
        # deleteButton11['background'] = '#fbb'
        # deleteButton11['cursor'] = 'hand2'
        # deleteButton11['activebackground'] = '#faa'
        # deleteButton11.pack(side = 'bottom', fill = 'x')


        self.note12 = Label(frame2, text = '', width = 20, height = 5)
        self.note12['background'] = '#ffb'
        self.note12.grid(row = 2, column = 3, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton12 = Button(self.note12, text = 'Delete')
        # deleteButton12['background'] = '#fbb'
        # deleteButton12['cursor'] = 'hand2'
        # deleteButton12['activebackground'] = '#faa'
        # deleteButton12.pack(side = 'bottom', fill = 'x')


        self.note13 = Label(frame2, text = '', width = 20, height = 5)
        self.note13['background'] = '#ffb'
        self.note13.grid(row = 3, column = 0, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton13 = Button(self.note13, text = 'Delete')
        # deleteButton13['background'] = '#fbb'
        # deleteButton13['cursor'] = 'hand2'
        # deleteButton13['activebackground'] = '#faa'
        # deleteButton13.pack(side = 'bottom', fill = 'x')

        self.note14 = Label(frame2, text = '', width = 20, height = 5)
        self.note14['background'] = '#ffb'
        self.note14.grid(row = 3, column = 1, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton14 = Button(self.note14, text = 'Delete')
        # deleteButton14['background'] = '#fbb'
        # deleteButton14['cursor'] = 'hand2'
        # deleteButton14['activebackground'] = '#faa'
        # deleteButton14.pack(side = 'bottom', fill = 'x')

        self.note15 = Label(frame2, text = '', width = 20, height = 5)
        self.note15['background'] = '#ffb'
        self.note15.grid(row = 3, column = 2, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton15 = Button(self.note15, text = 'Delete')
        # deleteButton15['background'] = '#fbb'
        # deleteButton15['cursor'] = 'hand2'
        # deleteButton15['activebackground'] = '#faa'
        # deleteButton15.pack(side = 'bottom', fill = 'x')

        self.note16 = Label(frame2, text = '', width = 20, height = 5)
        self.note16['background'] = '#ffb'
        self.note16.grid(row = 3, column = 3, sticky = 'nesw', pady = 5, padx = 5)
        # deleteButton16 = Button(self.note16, text = 'Delete')
        # deleteButton16['background'] = '#fbb'
        # deleteButton16['cursor'] = 'hand2'
        # deleteButton16['activebackground'] = '#faa'
        # deleteButton16.pack(side = 'bottom', fill = 'x')

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
        """
        Show the notes of the database in the interface.
        First validate if the notes exits else
        """
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
