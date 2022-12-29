from PIL import Image

mac = Image.open('images/example.jpg')
# print(mac.show())
print(mac.size)
# mac.filename
# mac.format_description


wid, hei = mac.size

halfway = wid / 2

x = halfway - 200
w = halfway + 200
y = 800
h = hei
print(mac.crop((x, y, w, h)).show())

pencils = Image.open('images/pencils.jpg')


print(pencils.size)

width, height = pencils.size

# x and y are staring points
x = 0
y = 0

w = width / 3
h = height / 10

print(pencils.crop((x, y, w, h)).show())

# bottom pencils

x = 0
y = 0

#  these are coordinates and so h iss now 1300

print(pencils.crop((x, 1100, w, height)).show())
