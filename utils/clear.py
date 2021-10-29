"""
This module have
functions for clean the inputs of the interface.
"""

from tkinter import END, Entry

def clearInput(input):
	"""
	Clean the input pass for
	parameter
	"""
	# validating if is Entry or Text object
	if isinstance(input, Entry):
		input.set('')
	else:
		# cleaning
		input.delete('1.0', END)