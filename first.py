from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root= Tk()
root.geometry("1800x800")
root.title("Image Editor")

# canvas = Canvas(root, width=800, height=500)
# canvas.pack()

#Frames defined
image_frame = LabelFrame(root, padx = 10, pady = 10)        # frame where image is placed
image_frame.place(relx = 0.3, rely = 0.5, anchor= CENTER)
colour_change_frame = LabelFrame(root, text = "Image Editor", padx = 10, pady = 10)
colour_change_frame.place(relx = 0.85, rely = 0.4, anchor = NE)


my_img = Image.open("Images/cat.png")
my_img = my_img.resize((500,450))
img_tk = ImageTk.PhotoImage(my_img.resize((500,450)))
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
	# filename = filedialog.askopenfile(initialdir="C:/Users/patel/gui/Images/", title="Select an Image", filetypes=filetypes)
	filename = "Images/dog.png"
	my_img = Image.open(filename)
	my_img = my_img.resize((500,450))
	img_tk = ImageTk.PhotoImage(my_img.resize((500,450)))
	image_show = Label(image_frame, image = img_tk)
	image_show.pack()


def saveImage():
    global my_img

    filename = filedialog.asksaveasfilename(initialdir= "/Images", title = "Save an Image", filetypes=(("png image", "*.png"), ("jpg image", "*.jpg")), defaultextension=(".png"))
    my_img.save(filename)
    


button1=Button(root,text="Open File", command = openImage)
button1.place(relx=0.0,rely=0.0)

button2=Button(root,text="Save File", command = saveImage)
button2.place(relx=0.05,rely=0.0)

button3=Button(root,text="Change to black and white")
button3.place(relx=0.85,rely=0.1)
button4=Button(root,text="Select area to crop")
button4.place(relx=0.8,rely=0.2)
button5=Button(root,text="Apply crop")
button5.place(relx=0.9,rely=0.2)
button6=Button(root,text="Flip Horizontally")
button6.place(relx=0.8,rely=0.3)
button7=Button(root,text="Flip vertically")
button7.place(relx=0.9,rely=0.3)
button8=Button(root,text="Rotate left")
button8.place(relx=0.8,rely=0.4)
button9=Button(root,text="Rotate right")
button9.place(relx=0.9,rely=0.4)
button10=Button(root,text="Apply Saturation")
button10.place(relx=0.9,rely=0.5)
button11=Button(root,text="Apply Sharpness")
button11.place(relx=0.9,rely=0.55)
button12=Button(root,text="Apply Exposure")
button12.place(relx=0.9,rely=0.6)
button13=Button(root,text="Apply Contrast")
button13.place(relx=0.9,rely=0.65)
button14=Button(root,text="Highlight Border")
button14.place(relx=0.85,rely=0.7)
button15=Button(root,text="Insert Text")
button15.place(relx=0.8,rely=0.85)
button16=Button(root,text="Fix Position")
button16.place(relx=0.9,rely=0.85)
label=Label(root)
label.place(relx=0.9,rely=0.8)
scale1=Scale(root, from_=1, to=50,orient=HORIZONTAL)
scale1.place(relx=0.8,rely=0.5)
scale2=Scale(root, from_=1, to=50,orient=HORIZONTAL)
scale2.place(relx=0.8,rely=0.55)
scale3=Scale(root, from_=1, to=50,orient=HORIZONTAL)
scale3.place(relx=0.8,rely=0.6)
scale4=Scale(root, from_=1, to=50,orient=HORIZONTAL)
scale4.place(relx=0.8,rely=0.65)
root.mainloop()
