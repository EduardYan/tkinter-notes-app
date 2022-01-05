"""
This module have functions for show
messsages in the interface.
"""
from tkinter import messagebox

def notNotes():
	"""
	Show a message window saying that
	not there notes.
	"""
	messagebox.showinfo('Notes', 'Not there. Add a new Note.')

def stopNotes():
	"""
	Show a message window warning
	that the notes view is full.
	"""
	messagebox.showwarning('Notes', 'Space max for thess notes.')

def showAbout():
	"""
	Show the window
	with information about the program.
	"""
	messagebox.showinfo('Add Notes App', 'Notes App is a small program for\nadd notes for remenber some task or things.')

def noValidContent():
	"""
	Show a window warning
	beacause the note is empty.
	"""
	messagebox.showwarning('Notes', 'The content of the note is empty.\nAdd some content.')