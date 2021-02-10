#This is a simple app which lets you open multiple applications from one place without navigating to the particular folder. All from one place.

import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps=[]  #Taking the app list

if os.path.isfile('apps.txt'):
    with open('apps.txt','r') as f:
        tempApps= f.read()
        #print(tempApps)
        tempApps= tempApps.split(',')
        apps=[i for i in tempApps if i.strip()]




def addApp():
    for widget in frame.winfo_children():
        widget.destroy()            #Clearing the screen
    filename=filedialog.askopenfilename(initialdir="/",title="Select File", filetypes=(("executables", "*.exe"), ("all files","*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label= tk.Label(frame, text=app, bg="gray")
        label.pack()



def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame= tk.Frame(root, bg="white")
frame.place(relwidth=0.8,relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File" , padx=10,pady=5, fg="white" , bg="#263D42", command=addApp)

openFile.pack()

RunApps = tk.Button(root, text="Run Apps" , padx=10,pady=5, fg="white" , bg="#263D42" , command=runApps)

RunApps.pack()

for app in apps:
    label=tk.label(frame, text=App)
    label.pack()
root.mainloop()


with open('apps.txt','w') as f:
    for app in apps:
        f.write(app + ',')