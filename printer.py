# --*--coding: utf-8--*--

# Error: cannot enter Chinese with Tkinter
# Solution: brew reinstall python3 --with-tcl-tk
# Reference:
# - https://www.jianshu.com/p/f9e30bdc5806
# - https://www.python.org/download/mac/tcltk/#activetcl-8-5-18-0

# 提取复姓
# Reference:
# - https://jingyan.baidu.com/article/17bd8e52121bf885ab2bb812.html


# import packages
import csv
import os

import tkinter as tk

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# surname with two Chinese characters
double_surnames_str = """
欧阳、太史、端木、上官、司马、东方、独孤、南宫、万俟、
闻人、夏侯、诸葛、尉迟、公羊、赫连、澹台、皇甫、宗政、
濮阳、公冶、太叔、申屠、公孙、慕容、仲孙、钟离、长孙、
宇文、司徒、鲜于、司空、闾丘、子车、亓官、司寇、巫马、
公西、颛孙、壤驷、公良、漆雕、乐正、宰父、谷梁、拓跋、
夹谷、轩辕、令狐、段干、百里、呼延、东郭、南门、羊舌、
微生、公户、公玉、公仪、梁丘、公仲、公上、公门、公山、
公坚、左丘、公伯、西门、公祖、第五、公乘、贯丘、公皙、
南荣、东里、东宫、仲长、子书、子桑、即墨、达奚、褚师
"""
double_surnames = double_surnames_str.replace('\n','').split('、')

# pictures
pics = ["长生禄位", "往生莲位-本宅", "往生莲位-亡灵", "往生莲位-氏门宗亲", "往生莲位-累劫今生"]

# font
# Mac
# fnt = "/Library/Font/simhei.ttf"
# Windows
fnt = "C:\Windows\Fonts\simhei.ttf"

# paramaters
params = [
    [340, 0.44, 0.47],
    [140, 0.067, 0.53, 90, 0.795, 0.4],
    [260, 0.067, 0.55],
    [260, 0.067, 0.55, 230, 0.456, 0.413, 0.415],
    [260, 0.065, 0.55],
]

def split_surname(name):
    surname = name[0:2]
    if surname in double_surnames:
        return surname
    else:
        surname = name[0]
        return surname

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
    font1 = ImageFont.truetype(fnt, params[choice][0])
    draw.text((im.size[0] * params[choice][1], im.size[1] * params[choice][2]), name, (0, 0, 0), font=font1)
    if choice==1:
        font2 = ImageFont.truetype(fnt, params[choice][3])
        draw.text((im.size[0] * params[choice][4], im.size[1] * params[choice][5]), address, (0, 0, 0), font=font2)
    elif choice==3:
        font2 = ImageFont.truetype(fnt, params[choice][3])
        surname = split_surname(e1.get())
        if len(surname)==1:
            t = 4
        elif len(surname)==2:
            t = 6
        draw.text((im.size[0] * params[choice][t], im.size[1] * params[choice][5]), surname, (0, 0, 0), font=font2)

    if not os.path.exists('target'):
        os.mkdir('target')
    im.save("./target/%s_%s_%s.jpg"%(choice, e1.get(), e2.get()))

    # Write information into csv files with GBK encoding
    if not os.path.exists('info.csv'):
        with open('info.csv', 'w', encoding='GBK', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['姓名','家庭地址','图片'])
    with open('info.csv','a', encoding='GBK', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([e1.get(),e2.get(),pics[choice]])

def gen_pics(vars):
    for i, var in enumerate(vars):
        if var.get()==1:
            gen_pic(i)
        elif var.get()==0:
            continue

    # Clear the Entry
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)


# main
if __name__=="__main__":
    master = tk.Tk()
    master.title('图片打印机')
    # master.geometry('800x600')

    tk.Label(master, text="姓名：").grid(row=0,sticky='W')
    tk.Label(master, text="家庭住址：").grid(row=1, sticky='W')

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.insert(10, "慕容测试")
    e2.insert(10, "测试地址")

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Label(master, text="请选择图片：").grid(row=3, sticky='W', columnspan=2)
    vars = []
    for i, pic in enumerate(pics):
        v = tk.IntVar()
        tk.Checkbutton(master, text=pic, variable=v).grid(row=4+i, sticky='W', columnspan=2, padx=10)
        vars.append(v)

    b1 = tk.Button(master, text='生成', command=lambda: gen_pics(vars)).grid(row=9, column=0, sticky='E')
    b2 = tk.Button(master, text='退出', command=master.quit).grid(row=9, column=1)

    tk.mainloop()