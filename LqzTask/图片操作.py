import os
from PIL import ImageColor,Image,ImageDraw,ImageFont

#rgb=ImageColor.getcolor('red','RGBA')
#print(rgb)

screen=Image.open('D:\\代码\\python块包\\image\\test_screen.png')
width,high=screen.size #filename/format/format_desription/save
print(width,high)

im=Image.new('RGBA',(100,100))#创建一个空白对象，坐标都从0开始
im.getpixel((0,0))
for r in range(50):
    for c in range(100):
        im.putpixel((r,c),(210,210,210))
for r in range(50,100):
    for c in range(100):
        im.putpixel((r,c),ImageColor.getcolor('darkgray', 'RGBA'))
im.save('D:\\代码\\python块包\\image\\background_RGBA.png')

newscreen=screen.crop((115, 125, 445, 460))#左上角，右下角坐标，副对角,crop对图像进行裁剪
newscreen.save('D:\\代码\\python块包\\image\\crop_test.png')

screencopy=screen.copy()
screencopy.paste(newscreen,(0,0))#粘贴操作直接在原图进行，需注意。粘贴坐标为图片左上角。
screencopy.save('D:\\代码\\python块包\\image\\copy_test.png')

a=screen.resize((int(width/2),int(high/2)))#resize不对原图进行修改，重置原图大小，仅接受常数
a.save('D:\\代码\\python块包\\image\\resize_test.png')

screen.rotate(90, expand=True).save('D:\\代码\\python块包\\image\\rotate_degree_expanded.png')
#若不加expand=True,则意味着在原图大小旋转,加上,则意味着旋转的同时放大，保证原图始终显示完全。

screen.transpose(Image.FLIP_LEFT_RIGHT).save('D:\\代码\\python块包\\image\\mirror_LR.png')#镜像左右
screen.transpose(Image.FLIP_TOP_BOTTOM).save('D:\\代码\\python块包\\image\\mirror_TD.png')#镜像上下

"""
#遍历文件添加icon
os.chdir(r'D:\代码\python块包\image')
os.makedirs(r'D:\代码\python块包\imagecopy',exist_ok=True)
MAX_SIZE=300
LOGO_NAME='caticons.png'
LOGO_names=Image.open(r'D:\代码\python块包\image\caticons.png')
WIDTH,HIGH=LOGO_names.size
print(WIDTH,HIGH)

for filename in os.listdir('.'):
    print(filename)
    if not(filename.endswith('.png') or filename.endswith('.img')) or filename==LOGO_NAME:
        continue
    im=Image.open(filename)
    width,high=im.size
    if width>MAX_SIZE and high>MAX_SIZE:
        if width>high:
            width=300
            high=int((MAX_SIZE/width)*high)
        else:
            high=300
            width=int((MAX_SIZE/high)*width)
        print(high,width)
        im=im.resize((width,high))
    im.paste(LOGO_names,(width - WIDTH,high - HIGH)) #第三个参数可以选择是否将icon设置为透明的
    im.save(r'D:\代码\python块包\imagecopy\%s'%(filename))
"""

"""
#在图片上绘制
im=Image.new('RGBA',(100,100))
draw=ImageDraw.Draw(im)
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),fill='brown')
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')

draw.text((20, 50), 'Hello', fill='purple')
draw.text((10, 50), 'Howdy', fill='gray')
im.save(r'D:\代码\python块包\image\sss.png')
"""




