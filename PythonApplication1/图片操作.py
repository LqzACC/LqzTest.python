from PIL import ImageColor,Image

#rgb=ImageColor.getcolor('red','RGBA')
#print(rgb)

screen=Image.open('D:\\代码\\python块包\\test_screen.png')
width,high=screen.size
print(width,high)

im=Image.new('RGBA',(100,100))
im.getpixel((0,0))
for r in range(50):
    for c in range(100):
        im.putpixel((r,c),(210,210,210))
for r in range(50,100):
    for c in range(100):
        im.putpixel((r,c),ImageColor.getcolor('darkgray', 'RGBA'))
im.save('D:\\代码\\python块包\\background_RGBA.png')

newscreen=screen.crop((115, 125, 445, 460))#左上角，右下角坐标，副对角,crop对图像进行裁剪
newscreen.save('D:\\代码\\python块包\\crop_test.png')

screencopy=screen.copy()
screencopy.paste(newscreen,(0,0))#粘贴操作直接在原图进行，需注意。粘贴坐标为图片左上角。
screencopy.save('D:\\代码\\python块包\\copy_test.png')

a=screen.resize((int(width/2),int(high/2)))#resize不对原图进行修改，重置原图大小
a.save('D:\\代码\\python块包\\resize_test.png')

screen.rotate(6, expand=True).save('D:\\代码\\python块包\\rotate_degree_expanded.png')
#若不加expand=True,则意味着在原图大小旋转,加上,则意味着旋转的同时放大，保证原图始终显示完全。

screen.transpose(Image.FLIP_LEFT_RIGHT).save('D:\\代码\\python块包\\mirror_LR.png')#镜像左右
screen.transpose(Image.FLIP_TOP_BOTTOM).save('D:\\代码\\python块包\\mirror_TD.png')#镜像上下


