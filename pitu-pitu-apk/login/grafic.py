import tkinter as tk

def login_window():
    window = tk.Tk()
    window.geometry("500x500")
    window.resizable(False, False)
    window.title("Login")
    window.configure()


    name = tk.Entry().place(x=100 ,y=100)
    password = tk.Entry().place(x=100 ,y=200)
    submit = tk.Button(text="submit").place(x=100, y=300)



    window.mainloop()

login_window()