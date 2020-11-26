from tkinter import *

spell_window = Tk()

spell_window.title('Spell Table')

table = ['T', 'a', 'b', 'l', 'e']
count = 1

def spell_table():
   global count, table
   the_label.config(text=table[:count])

   if count < len(table):
      count += 1



the_label = Label(spell_window, width = 10, text = "", font = ('Arial', 30), bg = 'red')

the_button = Button(spell_window, text = 'Next letter', command = spell_table)

the_label.pack(padx = 0, pady = 0)

the_button.pack(padx = 40, pady = 0)

spell_window.mainloop()