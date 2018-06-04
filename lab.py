# --*--coding: utf-8--*--

# Reference:
# - https://www.jianshu.com/p/f9e30bdc5806
# - https://www.python.org/download/mac/tcltk/#activetcl-8-5-18-0

# Error: cannot enter Chinese
# Solution: brew reinstall python3 --with-tcl-tk


import tkinter as tk


def show_entry_fields():
   print("姓名: %s\n家庭住址: %s" % (e1.get(), e2.get()))


master = tk.Tk()
tk.Label(master, text="姓名").grid(row=0)
tk.Label(master, text="家庭住址").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = tk.Button(master, text='生成', command=show_entry_fields).grid(row=3, column=0)
b2 = tk.Button(master, text='退出', command=master.quit).grid(row=3, column=1)

tk.mainloop()


