"""
This is a test of the functions
module.
"""

import unittest
from text_functions import converted_text


class TestText(unittest.TestCase):

	def setUp(self):
		self.o = 'this \nis the data'
	def test_text(self):
		self.assertEqual(converted_text('this is the data'), self.o)
		print(self.o)
		# self.assertEqual(converted_text('hola como estan en la consola alksjdflkajsdflkja'), 'hola\n como estan en la consola')


if __name__ == '__main__':
	unittest.main()