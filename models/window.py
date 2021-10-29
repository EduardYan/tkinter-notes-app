"""
This is file have a class
for do a window with tkinter.
"""

from tkinter import Tk

class Window:
  def getWind(self):
    wind = Tk()
    return wind

  def __str__(self):
  	return 'This is a window with tkinter module.'