from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path

root = Tk()
root.title('My Album!')
root.iconbitmap('marshall_paw_patrol_canine_patrol_icon_263825.ico')
# Define the directory path
directory_path = Path(r'C:\Users\anit4\OneDrive\Desktop\sboot')

# List all files in the directory
items = [i for i in directory_path.iterdir() if i.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif']]  # Filter by image files

# Create a Text widget
text_widget = Text(root, height=30, width=80,state=DISABLED)
text_widget.grid(row=0, column=0, columnspan=3, padx=30, pady=30)

# Create a Label widget to display images
img_label = Label(root)
img_label.grid(row=0, column=0, columnspan=3, padx=60, pady=60)

i=[0]

status=Label(root,text=f"Image {i[0]+1} of Images {len(items)}\n")

def update(index):
    status.config(text=f"Image {index+1} of Images {len(items)}\n",font=('Helvetica', 12))

def show_img(index):
    global img_label  # Using global variable for image label
    if 0 <= index < len(items):
        update(index)
        img = ImageTk.PhotoImage(Image.open(items[index]).resize((600, 450), Image.LANCZOS))
        #Image.LANCZOS is a resampling filter used by the Pillow library for resizing images. It’s known for providing high-quality results when reducing the size of images
        img_label.config(image=img)
        img_label.image = img  # Keep a reference to avoid garbage collection


def fshow_img(i):
    if(i[0]==len(items)-1):
        return
    i[0]+=1
    show_img(i[0])
    
def bshow_img(i):
    if(i[0]==0):
        return
    i[0]-=1
    show_img(i[0])
# Create buttons
button_forward = Button(root, text='>>', padx=20, pady=10, command=lambda: fshow_img(i))
button_backward = Button(root, text='<<', padx=20, pady=10, command=lambda: bshow_img(i))
button_quit = Button(root, text='Exit', padx=20, pady=10, command=root.quit)

# Place buttons in the grid
button_backward.grid(row=2, column=0)
button_quit.grid(row=2, column=1)
button_forward.grid(row=2, column=2)
status.grid(row=1,column=1)
# Display the first image if available
if items:
    show_img(0)
else:
    # No images found
    no_image_label = Label(root, text="No images found in the directory.")
    no_image_label.grid(row=0, column=0, columnspan=3, padx=30, pady=30)

root.mainloop()
