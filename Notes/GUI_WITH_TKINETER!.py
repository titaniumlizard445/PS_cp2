#PS 1st CP2
import tkinter as tk



root = tk.Tk()

root.title("Testing")

root.configure(background="blue")

root.minsize(400,400)
root.maxsize(1200,1200)

root.geometry("300x300+100+100")

label = tk.Label(root,text="This is most definently working",font=("Comic Sans",15,"bold"))
label.config(fg="white",background="red")
label.pack()

root.count = 0
def add():
    root.count += 1
    tk.Label(root, text=root.count).pack()

#button magic

btn = tk.Button(root, text="make bigger!",command=add)
btn.pack()

#image = tk.PhotoImage(file="images/sad.jpeg")

#tk.Label(root, image=image).pack()

root.mainloop() #This is always the end of the widgets
