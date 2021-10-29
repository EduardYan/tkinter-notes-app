"""
This module have the class
database for do the connections
and query at database.
"""

import sqlite3

db_path = './database/notes.sqlite3'

class DataBase:
  def __init__(self, path):
    self.path = path
    self.con = sqlite3.connect(self.path)
    self.cur = self.con.cursor()

  def select(self, query):
    """
    Execute the query passed for paramater, at database
    """
    try:
      data = self.cur.execute(query)

      return data.fetchall()

    except sqlite3.OperationalError as e:
      print(e)

  def insert(self, query):
    try:
      self.cur.execute(query)

      self.con.commit()

    except sqlite3.OperationalError as e:
      print(e)

  def delete(self, query):
    try:
      self.cur.execute(query)

      self.con.commit()

    except sqlite3.OperationalError as e:
      print(e)


  def update(self, query):
    try:
      self.cur.execute(query)

      self.cur.commit()

    except sqlite3.OperationalError as e:
      print(e)

  def close(self):
    """
    Close the connection with the database.
    """
    self.cur.close()
    self.con.close()
