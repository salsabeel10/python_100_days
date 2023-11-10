from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip,json
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web=(web_entry.get()).capitalize()
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.askokcancel(title="Error",message="No Data File Found \nCreate New One")
    else:
        if web in data:
                email=data[web]['email']
                pasw=data[web]['password']
                messagebox.askokcancel(title=web,message=f"email:{email} \npassword:{pasw}\n")
        else:
            messagebox.askokcancel(title="Error",message="There is no such website saved")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list+= [choice(symbols) for char in range(randint(2, 4))]
    password_list+= [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password="".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=(web_entry.get()).capitalize()
    email=email_entry.get()
    password=pass_entry.get()
    data_dict={
        website:{
            "email":email,
            "password":password
        },
    }
    
    if len(website) == 0 or len(email) == 0 or len(password)==0:
        messagebox.askretrycancel(title="Error", message="Please Dont Miss a filed")
    else:
        try:
            #file load
            with open("data.json","r+") as data_file:
                data=json.load(data_file)    
        except FileNotFoundError:
            #except error
            with open("data.json","w") as data_file:
                json.dump(data_dict,data_file,indent=4)
        else:
            #no error update data
            data.update(data_dict)
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(padx=45,pady=45)

canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
pass_img=PhotoImage(file="day 29/logo.png")
canvas.create_image(100,100, image = pass_img)
canvas.grid(row=0,column=1)

web=Label(text="Website:")
web.grid(row=1,column=0)

web_entry=Entry(width=25)
web_entry.grid(row=1,column=1)
web_entry.focus()

search=Button(text="Search",highlightthickness=0,width=14,command=find_password)
search.grid(row=1,column=2)

email=Label(text="Email/Username:")
email.grid(row=2,column=0)

email_entry=Entry(width=43)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"salsabeelibrahim327@gmail.com")

passw=Label(text="Password:")
passw.grid(row=3,column=0)

pass_entry=Entry(width=25)
pass_entry.grid(row=3,column=1)

genr_pass=Button(text="Generate Password",highlightthickness=0,width=14,command=generate_password)
genr_pass.grid(row=3,column=2)

add=Button(text="Add", width=40,highlightthickness=0,command=save)
add.grid(row=4, column=1,columnspan=2)

window.mainloop()