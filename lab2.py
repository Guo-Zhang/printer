# --*--coding: utf-8--*--

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

#设置字体，如果没有，也可以不设置
font1 = ImageFont.truetype("/Library/Fonts/simhei.ttf",100)
font2 = ImageFont.truetype("/Library/Fonts/simhei.ttf",80)

#打开底版图片
imageFile = "base.jpg"
im=Image.open(imageFile)

# 在图片上添加文字
name = u'测\n试'
address = u'测\n试\n地\n址'

draw = ImageDraw.Draw(im)
draw.text((im.size[0]*0.085, im.size[1]*0.6), name, (0,0,0), font=font1)
draw.text((im.size[0]*0.8, im.size[1]*0.4), address, (0,0,0), font=font2)

# 保存
im.save("target.jpg")