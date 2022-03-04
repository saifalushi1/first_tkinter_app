import tkinter
from tkinter import filedialog, Text
import os, sys, subprocess

from click import command

root = tkinter.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    #add conditional to check if user is using windows
    #if using windows add filetypes tuple ( filetypes=[("All Files", "*.*")])
    filename = filedialog.askopenfilename(initialdir="~", title="Select File")

    apps.append(filename)
    print(filename)
    for x in apps:
        label = tkinter.Label(frame, text=x, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        if os.name == "nt":
            os.startfile(app)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, app])

canvas = tkinter.Canvas(root, height=500, width=500)
canvas.pack()

frame = tkinter.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tkinter.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="grey", command=addApp)
openFile.pack()

appsToOpen = tkinter.Button(root, text="Run Selected Apps", padx=10, pady=5, fg="white", bg="grey", command=runApps)
appsToOpen.pack()

for app in apps:
    label = tkinter.Label(frame, text=app)
    label.pack()
root.mainloop()

with open('save.txt', "w") as f:
    for app in apps:
        f.write(app + ",")