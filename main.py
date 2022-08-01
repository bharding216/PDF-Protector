#PDF Protector App
#this is a branch to use tkinter to collect user input

#start in the command prompt with "pip3 install PyPDF2"
#also, pip3 install tk

from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
import tkinter as tk
from tkinter import *

#create the window
window = tk.Tk()
window.geometry("400x200")

#declaring string variables to store the file name and password
file_name = tk.StringVar()
secret_name = tk.StringVar()

#defining a function that will get the file name and password
#and encrypt the PDF
def encrypt():
    file = file_name.get()
    secret = secret_name.get()
    
    reader = PdfReader(file + ".pdf")
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add a password to the new PDF
    writer.encrypt(secret)

    # Save the new PDF to a file
    with open(file + "-encrypted.pdf", "wb") as f:
        writer.write(f)

#create the main window label
window.title("PDF Protector App")
label_title = tk.Label(text="PDF Protector App", font=('Arial', 12))

#create the label and entry box to collect the filename, and
#save the input as "filename"
label_filename = tk.Label(text="Enter File Name:")
filename = tk.Entry(width=30, textvariable=file_name)

#create the label and entry box to collect the password, and
#save the input as "secret_name"
label_password = tk.Label(text="Enter Password:")
password = tk.Entry(width=30, textvariable=secret_name)

#create the button that will call the encryption function above
submit = Button(window, text='Submit', width=20, command=encrypt)

#placing all the components within the window
label_title.pack(pady=(10, 0))
label_filename.pack(pady=(10, 0))
filename.pack()
label_password.pack(pady=(10, 0))
password.pack()
submit.pack(pady=(20,0))

#performing an infinite loop for the 
#window to display
window.mainloop()