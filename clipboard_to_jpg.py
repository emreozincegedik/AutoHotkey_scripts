from PIL import ImageGrab

img = ImageGrab.grabclipboard()
img.save('C:\\Users\\ZeuS\\Desktop\\paste.jpg', 'JPEG')