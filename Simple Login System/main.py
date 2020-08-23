from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.uname= StringVar()
        self.psw=StringVar()

        bg_image = Image.open(fp="gallery/bg.jpg", mode="r").resize((1350, 700), Image.ANTIALIAS)
        self.bg_icon = ImageTk.PhotoImage(bg_image)

        pro_image = Image.open(fp="gallery/profile.png", mode="r").resize((120, 120), Image.ANTIALIAS)
        self.user_img = ImageTk.PhotoImage(pro_image)

        pro_icon = Image.open(fp="gallery/profile_icon.png", mode="r").resize((25, 25), Image.ANTIALIAS)
        self.user_icon = ImageTk.PhotoImage(pro_icon)

        pass_icon = Image.open(fp="gallery/lock.png", mode="r").resize((25, 25), Image.ANTIALIAS)
        self.pass_icon = ImageTk.PhotoImage(pass_icon)

        #-----Variables-------#
        self.uname= StringVar()
        self.psw=StringVar()

        bg_lbl = Label(self.root,image=self.bg_icon).pack()
        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="black",fg="yellow")
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        logolbl = Label(Login_Frame,image=self.user_img,bd=0)
        logolbl.grid(row=0,columnspan=2,pady=20)

        userlbl = Label(Login_Frame, text="Username", image=self.user_icon, compound=LEFT,font=("times new roman",20,"bold"),bg="white")
        userlbl.grid(row=1,column=0,padx=20,pady=10)

        txtuser = Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        passlbl = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT,font=("times new roman",20,"bold"),bg="white")
        passlbl.grid(row=2,column=0,padx=20,pady=10)

        txtpass = Entry(Login_Frame,bd=5,textvariable=self.psw,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)

        btn_log=Button(Login_Frame,text="Login",width=15,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)

    def login(self):
        if self.uname.get()=="" or self.psw.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.uname.get()=="Shakir" and self.psw.get()=="12345":
            messagebox.showinfo("Successful",f"Welcome {self.uname.get()}")
        else:
            messagebox.showerror("Error","Invalid Username or Password")

        
root = Tk()
obj=Login_System(root)
root.mainloop()