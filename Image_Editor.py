from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageEnhance, ImageFilter, ImageFont, ImageDraw
from PIL.ImageFilter import CONTOUR, EMBOSS

root= Tk()
root.geometry("1800x800")
root.title("Image Editor")

# canvas = Canvas(root, width=800, height=500)
# canvas.pack()

#Frames defined
image_frame = LabelFrame(root, padx = 10, pady = 10)        # frame where image is placed
image_frame.place(relx = 0.3, rely = 0.5, anchor= CENTER)
#image_frame.place(relx = 0.7, rely = 0.7, anchor= CENTER)
colour_change_frame = LabelFrame(root, text = "Image Editor", padx = 10, pady = 10)
colour_change_frame.place(relx = 0.85, rely = 0.5, anchor = NE)

size_x=650
size_y=650

my_img = Image.open("Images/cat.png")
#my_img = my_img.resize((500,450))
my_img = my_img.resize((size_x,size_x))
img_tk = ImageTk.PhotoImage(my_img.resize((size_x,size_x)))
image_show = Label(image_frame, image = img_tk)
image_show.pack()


def openImage():
	global my_img
	global image_show
	global img_tk
	
	filetypes = (
		('All Picture Files', ['*.png', '*.jpg', '*.jpeg', '*.bmp']),
		('JPEG (*.jpeg)', '*.jpeg'),
		('JPG (*.jpg)', '*.jpg'),
		('PNG (*.png)', '*.png'),
		('BMP (*.bmp)', '*.bmp'),
		('All Files', '*.*')
	)	

	image_show.pack_forget()
	filename = filedialog.askopenfile(initialdir="/Images", title="Select an Image", filetypes=filetypes)
	# filename = "Images/dog.png"
	my_img = Image.open(filename.name)
	my_img = my_img.resize((size_x,size_x))
	img_tk = ImageTk.PhotoImage(my_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def saveImage():
    global my_img

    filename = filedialog.asksaveasfilename(initialdir= "/Images", title = "Save an Image", filetypes=(("png image", "*.png"), ("jpg image", "*.jpg")), defaultextension=(".png"))
    my_img.save(filename)

def bwImage():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	my_img = my_img.convert("L")
	img_tk = ImageTk.PhotoImage(my_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()

def flipH():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	my_img = my_img.transpose(Image.FLIP_LEFT_RIGHT)
	img_tk = ImageTk.PhotoImage(my_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def flipV():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	my_img = my_img.transpose(Image.FLIP_LEFT_RIGHT)
	my_img = my_img.transpose(Image.FLIP_TOP_BOTTOM)
	img_tk = ImageTk.PhotoImage(my_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def rotateL():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	my_img = my_img.transpose(Image.ROTATE_90)
	img_tk = ImageTk.PhotoImage(my_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()

def rotateR():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	my_img = my_img.transpose(Image.ROTATE_270)
	img_tk = ImageTk.PhotoImage(my_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def Saturation():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	converter = ImageEnhance.Color(my_img)
	tmp_img = converter.enhance(scale1.get())
	img_tk = ImageTk.PhotoImage(tmp_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def Sharpness():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	converter = ImageEnhance.Sharpness(my_img)
	tmp_img = converter.enhance(scale2.get())
	img_tk = ImageTk.PhotoImage(tmp_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def Brightness():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	converter = ImageEnhance.Brightness(my_img)
	tmp_img = converter.enhance(scale3.get())
	img_tk = ImageTk.PhotoImage(tmp_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def Contrast():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	converter = ImageEnhance.Contrast(my_img)
	tmp_img = converter.enhance(scale4.get())
	img_tk = ImageTk.PhotoImage(tmp_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def Contour():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	my_img = my_img.filter(CONTOUR)
	img_tk = ImageTk.PhotoImage(my_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()



def Emboss():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	my_img = my_img.filter(EMBOSS)
	img_tk = ImageTk.PhotoImage(my_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def Resize():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	img_tk = ImageTk.PhotoImage(my_img.resize((round(my_img.size[0]*0.5), round(my_img.size[1]*0.5))))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def addText():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	text_font=ImageFont.truetype("arial.ttf", size=35)
	text_to_add=entry.get()
	draw_img=ImageDraw.Draw(my_img)
	draw_img.text((150, 600), text_to_add, ("red"), font=text_font)
	img_tk = ImageTk.PhotoImage(my_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def Crop():
	global my_img
	global image_show
	global img_tk

	image_show.pack_forget()
	my_img = my_img.crop((200,200,500,500))
	img_tk = ImageTk.PhotoImage(my_img.resize((size_x,size_x)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()

	


button1=Button(root,text="Open File", command=openImage)
button1.place(relx=0.0,rely=0.0)

button2=Button(root,text="Save File", command=saveImage)
button2.place(relx=0.05,rely=0.0)

button3=Button(root,text="Change to black and white", command=bwImage)
button3.place(relx=0.8,rely=0.1)
button18=Button(root,text="Resize image", command=Resize)
button18.place(relx=0.9,rely=0.1)

button5=Button(root,text="Apply crop", command=Crop)
button5.place(relx=0.85,rely=0.2)

button6=Button(root,text="Flip Horizontally", command=flipH)
button6.place(relx=0.8,rely=0.3)
button7=Button(root,text="Flip vertically", command=flipV)
button7.place(relx=0.9,rely=0.3)
button8=Button(root,text="Rotate left", command=rotateL)
button8.place(relx=0.8,rely=0.4)
button9=Button(root,text="Rotate right", command=rotateR)
button9.place(relx=0.9,rely=0.4)

scale1=Scale(root, from_=0, to=2, resolution=0.2, orient=HORIZONTAL)
scale1.set(1)
scale1.place(relx=0.8,rely=0.5)

scale2=Scale(root, from_=-3, to=5,resolution=0.2, orient=HORIZONTAL)
scale2.set(1)
scale2.place(relx=0.8,rely=0.55)


scale3=Scale(root, from_=0, to=2, resolution=0.2, orient=HORIZONTAL)
scale3.set(1)
scale3.place(relx=0.8,rely=0.6)

scale4=Scale(root, from_=-2, to=3, resolution=0.2, orient=HORIZONTAL)
scale4.set(1)
scale4.place(relx=0.8,rely=0.65)

button10=Button(root,text="Apply Saturation", command=Saturation)
button10.place(relx=0.9,rely=0.5)
button11=Button(root,text="Apply Sharpness", command=Sharpness)
button11.place(relx=0.9,rely=0.55)
button12=Button(root,text="Apply Brightness", command=Brightness)
button12.place(relx=0.9,rely=0.6)
button13=Button(root,text="Apply Contrast", command=Contrast)
button13.place(relx=0.9,rely=0.65)

button14=Button(root,text="Contour Image", command=Contour)
button14.place(relx=0.8,rely=0.75)
button15=Button(root,text="Emboss Image", command=Emboss)
button15.place(relx=0.9,rely=0.75)

entry=Entry(root, relief=SUNKEN, width=40)
entry.place(relx=0.8,rely=0.8)


button16=Button(root,text="Insert Text", command=addText)
button16.place(relx=0.85,rely=0.85)




root.mainloop()
