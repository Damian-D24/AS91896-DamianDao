import tkinter as tk
root = tk.Tk()

root.title("The Best Program")

first_title=tk.Label(root, text="Welcome to 12CSC")
first_title.grid(row=0, column=0)

stop_button=tk.Button(root, text="Stop", width=30, command=root.destroy, bg="red", fg="yellow", activebackground="blue", activeforeground="white")
stop_button.grid(row=1, column=0)

second_title=tk.Button(root, text="Who are you?", bg="green", fg="white", activebackground="pink", activeforeground="black")
second_title.grid(row=2, column=0)

firstname=tk.Label(root, text="First name:", bg="red", fg="yellow", activebackground="blue", activeforeground="white")
secondname=tk.Label(root, text="Second name:", bg="red", fg="yellow", activebackground="blue", activeforeground="white")

firstname.grid(row=3, column=0)
secondname.grid(row=4, column=0)

name1=tk.Entry(root, bg="red", fg="yellow")
name2=tk.Entry(root, bg="red", fg="yellow")
name1.grid(row=3, column=1)
name2.grid(row=4, column=1)

root.mainloop()