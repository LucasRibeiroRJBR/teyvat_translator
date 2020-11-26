from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle

exp = " "

def press(num):
    global exp
    exp= exp + str(num)
    equation.set(exp)

def clear():
    global exp
    exp = " "
    equation.set(exp)

def backspace():
    global exp
    exp = entry.get()[:-1]
    equation.set(exp)

root = Tk()
root.title('Teyvat Translator')
style = ThemedStyle(root)
style.set_theme('yaru')

# IMAGES
img_title = PhotoImage(file='img/title.png')
img_a = PhotoImage(file="img/letters/a.png")
img_b = PhotoImage(file="img/letters/b.png")
img_c = PhotoImage(file="img/letters/c.png")
img_d = PhotoImage(file="img/letters/d.png")
img_e = PhotoImage(file="img/letters/e.png")
img_f = PhotoImage(file="img/letters/f.png")
img_g = PhotoImage(file="img/letters/g.png")
img_h = PhotoImage(file="img/letters/h.png")
img_i = PhotoImage(file="img/letters/i.png")
img_j = PhotoImage(file="img/letters/j.png")
img_k = PhotoImage(file="img/letters/k.png")
img_l = PhotoImage(file="img/letters/l.png")
img_m = PhotoImage(file="img/letters/m.png")
img_n = PhotoImage(file="img/letters/n.png")
img_o = PhotoImage(file="img/letters/o.png")
img_p = PhotoImage(file="img/letters/p.png")
img_q = PhotoImage(file="img/letters/q.png")
img_r = PhotoImage(file="img/letters/r.png")
img_s = PhotoImage(file="img/letters/s.png")
img_t = PhotoImage(file="img/letters/t.png")
img_u = PhotoImage(file="img/letters/u.png")
img_v = PhotoImage(file="img/letters/v.png")
img_w = PhotoImage(file="img/letters/w.png")
img_x = PhotoImage(file="img/letters/x.png")
img_y = PhotoImage(file="img/letters/y.png")
img_z = PhotoImage(file="img/letters/z.png")

# ELEMENTS
title = ttk.Label(root, image=img_title)

# BUTTONS
s = ttk.Style()
s.configure('my.TButton', font=('Arial', 14, 'bold'))

bt_a = ttk.Button(root, image=img_a, command=lambda : press('A'))
bt_b = ttk.Button(root, image=img_b, command=lambda : press('B'))
bt_c = ttk.Button(root, image=img_c, command=lambda : press('C'))
bt_d = ttk.Button(root, image=img_d, command=lambda : press('D'))
bt_e = ttk.Button(root, image=img_e, command=lambda : press('E'))
bt_f = ttk.Button(root, image=img_f, command=lambda : press('F'))
bt_g = ttk.Button(root, image=img_g, command=lambda : press('G'))
bt_h = ttk.Button(root, image=img_h, command=lambda : press('H'))
bt_i = ttk.Button(root, image=img_i, command=lambda : press('I'))
bt_j = ttk.Button(root, image=img_j, command=lambda : press('J'))
bt_k = ttk.Button(root, image=img_k, command=lambda : press('K'))
bt_l = ttk.Button(root, image=img_l, command=lambda : press('L'))
bt_m = ttk.Button(root, image=img_m, command=lambda : press('M'))
bt_n = ttk.Button(root, image=img_n, command=lambda : press('N'))
bt_o = ttk.Button(root, image=img_o, command=lambda : press('O'))
bt_p = ttk.Button(root, image=img_p, command=lambda : press('P'))
bt_q = ttk.Button(root, image=img_q, command=lambda : press('Q'))
bt_r = ttk.Button(root, image=img_r, command=lambda : press('R'))
bt_s = ttk.Button(root, image=img_s, command=lambda : press('S'))
bt_t = ttk.Button(root, image=img_t, command=lambda : press('T'))
bt_u = ttk.Button(root, image=img_u, command=lambda : press('U'))
bt_v = ttk.Button(root, image=img_v, command=lambda : press('V'))
bt_w = ttk.Button(root, image=img_w, command=lambda : press('W'))
bt_x = ttk.Button(root, image=img_x, command=lambda : press('X'))
bt_y = ttk.Button(root, image=img_y, command=lambda : press('Y'))
bt_z = ttk.Button(root, image=img_z, command=lambda : press('Z'))
bt_backspace = ttk.Button(root, text='BACKSPACE', command=backspace, width=25, style='my.TButton')
bt_clear = ttk.Button(root, text='CLEAR', command=clear, width=6, style='my.TButton')
bt_space = ttk.Button(root, text='SPACE', command=lambda : press(' '), width=93, style='my.TButton')

# ENTRY
equation = StringVar()
entry = ttk.Entry(root,
                  state='readonly',
                  textvariable=equation,
                  width=50,
                  font=('Lucida Sans', 25, 'bold'))

# GRIDs
title.grid(row=0, columnspan=10)
bt_a.grid(row=1, column=0)
bt_b.grid(row=1, column=1)
bt_c.grid(row=1, column=2)
bt_d.grid(row=1, column=3)
bt_e.grid(row=1, column=4)
bt_f.grid(row=1, column=5)
bt_g.grid(row=1, column=6)
bt_h.grid(row=1, column=7)
bt_i.grid(row=1, column=8)
bt_j.grid(row=1, column=9)
bt_k.grid(row=2, column=0)
bt_l.grid(row=2, column=1)
bt_m.grid(row=2, column=2)
bt_n.grid(row=2, column=3)
bt_o.grid(row=2, column=4)
bt_p.grid(row=2, column=5)
bt_q.grid(row=2, column=6)
bt_r.grid(row=2, column=7)
bt_s.grid(row=2, column=8)
bt_t.grid(row=2, column=9)
bt_u.grid(row=3, column=0)
bt_v.grid(row=3, column=1)
bt_w.grid(row=3, column=2)
bt_x.grid(row=3, column=3)
bt_y.grid(row=3, column=4)
bt_z.grid(row=3, column=5)
bt_backspace.grid(row=3, column=5, columnspan=9, ipady=22, padx=5)
bt_clear.grid(row=3, column=9, ipady=22)
bt_space.grid(row=4, column=0, columnspan=10, ipady=20)
entry.grid(row=5, columnspan=10, ipady=10, pady=10)

root.mainloop()
