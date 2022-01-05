"""
This is the principal file for
execute the interface and the program.
"""

from models.window import Window
from ui import UI

if __name__ == '__main__':
    # executing
    wind = Window().getWind()

    UI(wind)

    wind.mainloop()
