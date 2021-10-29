"""
This file have functions utils
for use.
"""

def converted_text(text):
	"""
	Return the text passed for parameter
	but with some tabs for show in the interface,
	of a better form.
	"""
	# validating for do the modifications
	if len(text) > 10:
		list_text = [l for l in text]

		try:
			list_text.insert(15, '\n')
			list_text.insert(20, '\n')

		except:
			pass

		new_text = ''

		for e in list_text:
			new_text += e

		return new_text

	# en caso no sea mayor a diez
	return text