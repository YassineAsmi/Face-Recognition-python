import tkinter as tk
import os
import subprocess
root = tk.Tk()
root.geometry("1000x800")

def image(smp):
    img = tk.PhotoImage(file="image.png")
    img = img.subsample(smp, smp)
    return img
 
def add_new_face():
    os.system("python face_dataset.py") 
def training_ai():
    os.system("python face_training.py") 
def run_app():
    os.system("python face_recognition.py") 
def open_unknown():
    subprocess.Popen(r'explorer "C:\Users\yassi\Desktop\Face-Recognition-in-Python\Unknown_people"')

but = tk.Button(
    root,
    bd=0,
    compound=tk.CENTER,
    bg="white",
    fg="red",
    activeforeground="pink",
    activebackground="white",
    font="arial 30",
    text="Add New Face",
    pady=10,
    command=add_new_face
    )
but1 = tk.Button(
    root,
    bd=0,
    relief="groove",
    compound=tk.CENTER,
    bg="white",
    fg="red",
    activeforeground="pink",
    activebackground="white",
    font="arial 30",
    text="AI Training ...",
    pady=10,
    command=training_ai
    # width=300
    )
but2 = tk.Button(
    root,
    bd=0,
    relief="groove",
    compound=tk.CENTER,
    bg="white",
    fg="red",
    activeforeground="pink",
    activebackground="white",
    font="arial 28",
    text="Run Face Recognition",
    pady=10,
    # width=300
    command=run_app
    )
but3 = tk.Button(
    root,
    bd=0,
    relief="groove",
    compound=tk.CENTER,
    bg="white",
    fg="red",
    activeforeground="pink",
    activebackground="white",
    font="arial 28",
    text="UnAuthorized Picture",
    pady=10,
    command=open_unknown
    )
 
img = image(1) # 1=normal, 2=small, 3=smallest
but.config(image=img)
but.pack()
but1.config(image=img)
but1.pack()
but2.config(image=img)
but2.pack()
but3.config(image=img)
but3.pack()

root.mainloop()