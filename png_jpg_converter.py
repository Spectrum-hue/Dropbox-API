#This is a image converter program which convert PNG files to JPG files.
# Make sure to first click the import button and then the "PNG to JPG" button.
# Also make sure a PNG image is chosen.

import dropbox
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 250, bg = '#003153', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='PNG to JPG Tool', bg = 'azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

# Function for the 1st button & messagebox
def getPNG ():
    global im1

    # user will be directed to the filedialog to choose a picture
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
    
browseButton_PNG = tk.Button(text='Import PNG File', command=getPNG, bg='#b8860b', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_PNG)
MsgBox = tk.messagebox.showinfo('Import PNG File','Remember to choose a PNG file - A JPG file wont convert')

def convertToJPG ():
    global im1
    
    # user will be directed to the filedialog to save a picture
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)
    computer_path =  export_file_path
    path = Path(computer_path)
    
    # Your own access token inserted below
    dropbox_access_token= 'sl.AwRyETAmB-QIkSawT1sRi34BAUmcc0KI5JYvx_aQroXyOOgUW_Hs7z_xiOwy9O0jec-o31Nv8IQyCtmt50lEG06LZALOPYamPXHvTJMTFycmueckXGmfnL8vAKy5BgTWOHY_kGs-kis'    
    dropbox_path= "/{}".format(path.name)
    client = dropbox.Dropbox(dropbox_access_token)
    
    # If successful, the image will be sended to Dropbox via the V2 API.
    print("[SUCCESS] dropbox account linked")
    client.files_upload(open(path, "rb").read(), dropbox_path)
    print("[UPLOADED] {}".format(path))
    print(path.name)

saveAsButton_JPG = tk.Button(text='Convert PNG to JPG', command=convertToJPG, bg='#b8860b', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_JPG)
newMsgBox = tk.messagebox.showinfo("Remember to first click on the 'import PNG 'button' - If you have imported an image already ignore this message")
