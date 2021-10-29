"""
This module have
a class for use in ui.py
"""

class Note:
	"""
	Create a new Note with a content.
	"""
	def __init__(self, content):
		self.content = content

	def __getContent(self):
		"""
		Return the self.content passed
		for parameter in the contructor

		!!! This method is deprectaded.
		"""
		
		return self.content

	def __str__(self):
		return f'This is a note with content {self.content}'