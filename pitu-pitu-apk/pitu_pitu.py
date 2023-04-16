# biblioteki
import pymysql as mysql
import tkinter as tk

# login
# okno tkinter
def login_window():
    window = tk.Tk()
    window.geometry("500x500")
    window.resizable(False, False)
    window.title("Login")
    window.configure()

    global user
    class user:
        name = ""
        password = ""

    global name_var
    global password_var
    name_var = tk.StringVar()
    password_var = tk.StringVar()

    name = tk.Entry(textvariable=name_var).place(x=200 ,y=150)
    password = tk.Entry(textvariable=password_var).place(x=200 ,y=200)
    submit = tk.Button(text="sign in", command=login).place(x=200, y=240)

    name_description = tk.Label(text="name").place(x=140, y=150)
    password_description = tk.Label(text="password").place(x=140, y=200)

    window.mainloop()

# połączenie z BD
def sql():
    con = mysql.Connect(host='localhost', user='root', passwd='', db='pitu_pitu')
    cur = con.cursor()

    cur.execute("select * from users")  

    global args
    for args in cur:
        args

    cur.close()

# pabranie nazwy i hasła
def get_login():
    user.name = name_var.get()
    user.password = password_var.get()
    print(user.name, user.password)

# sprawdenie loginu
def check_login():
    get_login()
    if (user.name in args) and (user.password in args):
        print("jest taki user")
    else:
        print("nie ma takiego usera")
        user.name = tk.StringVar()
        user.password = tk.StringVar()

# uruchomienie aplikajcji
# def login():
#     sql()
#     check_login()
        
# login_window()

# koniec logowania



















# komunikator tekstowy
# okno tkinter
def apk_window():
    window = tk.Tk()
    window.geometry("800x500")
    window.resizable(False, False)
    window.title("Pitu pitu")

    header = tk.Canvas(
        window,
        height = 800,
        width = 40,
        bg = "yellow",
        border = 0
    ).place(x=758, y=0)
    
    container = tk.Canvas(
        window,
        height = 400,
        width = 680,
        border = 0
    ).place(x=40, y=40)

    add_mess = tk.Button(
        header,
        text="+"
    ).place(x=770, y=10)

    window.mainloop()

# połączenie z BD
def sql2():
    con = mysql.Connect(host='localhost', user='root', passwd='', db='pitu_pitu')
    global cur
    cur = con.cursor()
    cur.execute("select mess, name from messages, users")
    global napis

    for mess, name in cur:
        napis = name + " napisał/a: " + mess
        text = tk.Label(
            text = napis
        ).pack()

    cur.close()


def pitu_pitu():
    sql2()
    apk_window()

pitu_pitu()