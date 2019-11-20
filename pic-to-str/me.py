from PIL import Image

im1 = Image.open("D:/桌面/壁纸/1920x1080.jpg").convert('RGBA').resize((1920, 1080))
im2 = Image.open("D:/桌面/壁纸/下载 (6).jpg").convert('RGBA').resize((1920, 1080))
out = Image.alpha_composite(im1, im2)
im2.show()