from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image


#Class for login System


class Login_System:
    #Root is  name of window

    def __init__(self,root):
        self.root = root
        self.root.title("📲 Login System ❤")
        self.root.geometry("1350x700+0+0")


        #All Images
        self.bg_icon = ImageTk.PhotoImage(file="Images/Background.jpg")
        image_name = Image.open("open.png")
        image_name1 = Image.open("Images/v_avatar.png")
       #image_name.resize((10,10))

        self.user_icon = ImageTk.PhotoImage(image_name.resize((20,20)))
        self.pass_icon = ImageTk.PhotoImage(image_name1.resize((20,20)))
        self.logo_icon = PhotoImage(file="Images/assassin_avatar.png")

        #Variables for Usernama and Password
        self.uname = StringVar()
        self.password = StringVar()



        bg_lbl = Label(self.root,image = self.bg_icon)
        bg_lbl.pack()

        title=Label(self.root,text="Login System",font=("times new roman",30,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame = Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        logolbl = Label(Login_Frame,image = self.logo_icon).grid(row=0,column=0,columnspan=2 ,pady=20)


        lbluser = Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        textuser = Entry(Login_Frame,bd=5, textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)


        lblpass = Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        passuser = Entry(Login_Frame,bd=5,textvariable=self.password,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)

        btn_login = Button(Login_Frame,text="Login",width="15",command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10,padx=10)

    def login(self):
        if(self.uname.get()=="" or self.password.get()==""):
            messagebox.showerror("Error","All fields are required!")
        elif(self.uname.get()=="Ganesh" and self.password.get()=="Tiwari"):
            messagebox.showinfo(f"Welcome {self.uname.get()} You have done alot in this quarentine period keep it up")
        else:
            messagebox.showerror("Invalid Username or password")

root = Toplevel()
obj = Login_System(root)
root.mainloop()
