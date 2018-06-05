# --*--coding: utf-8--*--

# Error: cannot enter Chinese with Tkinter
# Solution: brew reinstall python3 --with-tcl-tk
# Reference:
# - https://www.jianshu.com/p/f9e30bdc5806
# - https://www.python.org/download/mac/tcltk/#activetcl-8-5-18-0

# 提取复姓
# Reference:
# - https://jingyan.baidu.com/article/17bd8e52121bf885ab2bb812.html


import tkinter as tk

import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# font
# Mac
# fnt = "/Library/Font/simhei.ttf"
# Windows
fnt = "C:\Windows\Fonts\simhei.ttf"

# paramaters
params = [
    [0.085, 0.5, 0.8, 0.25, 250, 150],
    [0.085, 0.6, 0.8, 0.4, 120, 80],
    [0.079, 0.6, 0.8, 0.25, 250, 150],
    [0.079, 0.6, 0.8, 0.25, 250, 150],
    [0.07, 0.6, 0.8, 0.25, 250, 150],
]
# todo: 字体调大一些；调整输入的数据，除了图1都是姓名，图3需要识别姓


def show_entry_fields():
    # To test whether the tkinter Entry is workable
    print("姓名: %s\n家庭住址: %s" % (e1.get(), e2.get()))

def row2column(x):
    result = ''
    for i in x:
        result+=i
        result+='\n'
    return result

def gen_pic(choice):
    im = Image.open('./base/base%s.jpg'%choice)

    name = row2column(e1.get())
    address = row2column(e2.get())

    draw = ImageDraw.Draw(im)
    font1 = ImageFont.truetype(fnt, params[choice][4])
    font2 = ImageFont.truetype(fnt, params[choice][5])
    draw.text((im.size[0] * params[choice][0], im.size[1] * params[choice][1]), name, (0, 0, 0), font=font1)
    draw.text((im.size[0] * params[choice][2], im.size[1] * params[choice][3]), address, (0, 0, 0), font=font2)

    # im.show()

    im.save("./target/%s_%s_%s.jpg"%(choice, e1.get(), e2.get()))


# main
if __name__=="__main__":
    master = tk.Tk()
    # master.geometry('800x600')

    tk.Label(master, text="姓名：").grid(row=0,sticky='W')
    tk.Label(master, text="家庭住址：").grid(row=1, sticky='W')

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.insert(10, "测试")
    e2.insert(10, "测试地址")

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    v = tk.IntVar()

    # todo: 改多选
    tk.Label(master, text="请选择图片：").grid(row=3, sticky='W', columnspan=2)
    tk.Radiobutton(master, text="长生禄位", variable=v, value=0).grid(row=4, sticky='W', columnspan=2, padx=10)
    tk.Radiobutton(master, text="往生莲位-本宅", variable=v, value=1).grid(row=5, sticky='W', columnspan=2, padx=10)
    tk.Radiobutton(master, text="往生莲位-亡灵", variable=v, value=2).grid(row=6, sticky='W', columnspan=2, padx=10)
    tk.Radiobutton(master, text="往生莲位-氏门宗亲", variable=v, value=3).grid(row=7, sticky='W', columnspan=2, padx=10)
    tk.Radiobutton(master, text="往生莲位-累劫今生", variable=v, value=4).grid(row=8, sticky='W', columnspan=2, padx=10)

    b1 = tk.Button(master, text='生成', command=lambda: gen_pic(v.get())).grid(row=9, column=0, sticky='E')
    b2 = tk.Button(master, text='退出', command=master.quit).grid(row=9, column=1)

    tk.mainloop()