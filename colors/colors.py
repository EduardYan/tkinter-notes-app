"""
This module have a function
for change the color of the cards
of the interface
"""

def changeColor(card, color):
	"""
	Change the color of the card passed
	for parameter
	"""
	card['background'] = color


def changeToRed(cards):
	"""
	Change to red the color
	"""
	for c in cards:
		if c['background'] != '#d9d9d9':
			changeColor(c, 'red')

def changeToBlue(cards):
	"""
	Change to blue the color
	"""
	for c in cards:
		if c['background'] != '#d9d9d9':
			changeColor(c, 'blue')

def changeToYellow(cards):
	"""
	Change to yellow the color
	"""
	for c in cards:
		if c['background'] != '#d9d9d9':
			changeColor(c, 'yellow')

def changeToOrange(cards):
	"""
	Change to orange the color
	"""
	for c in cards:
		if c['background'] != '#d9d9d9':
			changeColor(c, 'orange')


def changeToGreen(cards):
	"""
	Change to green the color
	"""
	for c in cards:
		if c['background'] != '#d9d9d9':
			changeColor(c, 'green')