from tkinter import *
from tkinter import ttk
import pymysql
import mysql.connector


class Student:
    def __init__(self,root):


        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")


        title = Label(self.root, text="Student Management System",bd=10,relief=GROOVE, font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        ################   Variables ##############
        self.rollNoVar=StringVar()
        self.nameVar=StringVar()
        self.classVar=StringVar()
        self.sectionVar=StringVar()
        self.contactVar=StringVar()
        self.addressVar=StringVar()
        self.dobVar=StringVar()



        #Manage Frame
        Manage_Frame = Frame(self.root,border=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=560)






        #Working for Manage Frame
        m_title = Label(Manage_Frame, text = "Manage Students",fg="white",bg="crimson", font = ("times new roman", 20,"bold"))
        m_title.grid(row=0,columnspan =2, pady=10, padx=10)





        #Roll No and its Input
        lbl_roll = Label(Manage_Frame, text = "Roll No",fg="white",bg="crimson", font = ("times new roman", 16,"bold"))
        lbl_roll.grid(row=1,column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame,textvariable = self.rollNoVar ,relief = GROOVE ,bg="white", font = ("times new roman", 14,"bold"))
        txt_Roll.grid(row=1,column=1, pady=10, padx=20, sticky="w")


        #Name

        lbl_Name = Label(Manage_Frame, text = "Name",fg="white",bg="crimson", font = ("times new roman", 16,"bold"))
        lbl_Name.grid(row=2,column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame,textvariable = self.nameVar ,relief = GROOVE ,bg="white", font = ("times new roman", 14,"bold"))
        txt_Name.grid(row=2,column=1, pady=10, padx=20, sticky="w")

        #Email
        lbl_Email = Label(Manage_Frame, text = "Email",fg="white",bg="crimson", font = ("times new roman", 16,"bold"))
        lbl_Email.grid(row=3,column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame,relief = GROOVE ,bg="white", font = ("times new roman", 14,"bold"))
        txt_Email.grid(row=3,column=1, pady=10, padx=20, sticky="w")

        #Gender

        lbl_Gender = Label(Manage_Frame, text = "Gender",fg="white",bg="crimson", font = ("times new roman", 16,"bold"))
        lbl_Gender.grid(row=4,column=0, pady=10, padx=20, sticky="w")


        combo_gender=ttk.Combobox(Manage_Frame,state='readonly',font = ("times new roman", 13,"bold"))
        combo_gender['values']=('Male','Female',"Other")
        combo_gender.grid(row=4,column=1, pady=10, padx=20, sticky="w")


        #Contact
        lbl_Contact = Label(Manage_Frame, text = "Contact No",fg="white",bg="crimson", font = ("times new roman", 16,"bold"))
        lbl_Contact.grid(row=5,column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame, textvariable = self.contactVar ,relief = GROOVE ,bg="white", font = ("times new roman", 14,"bold"))
        txt_Contact.grid(row=5,column=1, pady=10, padx=20, sticky="w")



        #D.O.B
        lbl_DOB = Label(Manage_Frame, text = "D.O.B",fg="white",bg="crimson", font = ("times new roman", 16,"bold"))
        lbl_DOB.grid(row=6,column=0, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame, textvariable = self.dobVar ,relief = GROOVE ,bg="white", font = ("times new roman", 14,"bold"))
        txt_DOB.grid(row=6,column=1, pady=10, padx=20, sticky="w")



        #Address
        lbl_Address = Label(Manage_Frame,text = "Address",fg="white",bg="crimson", font = ("times new roman", 16,"bold"))
        lbl_Address.grid(row=7,column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")


        #Button Frame
        Btn_Frame = Frame(Manage_Frame,border=4,relief=RIDGE,bg="crimson")
        Btn_Frame.place(x=10,y=500,width=430)

        Addbtn=Button(Btn_Frame, text="Add",command= self.add_student,width=10).grid(row=0,column=0,padx=10,pady=10)
        Update_btn=Button(Btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        Delete_btn=Button(Btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(Btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)




        ############################ This is end of Manage Frame ##################


        #Detail Frame
        Detail_Frame = Frame(self.root,border=4,relief=RIDGE,bg="blue")
        Detail_Frame.place(x=500,y=100,width=850,height=560)


        #Workin of Detail Frame


        lbl_Search = Label(Detail_Frame, text = "Search By",fg="white",bg="blue", font = ("times new roman", 16,"bold"))
        lbl_Search.grid(row=0,column=0, pady=10, padx=20, sticky="w")



        #Searching the Student

        combo_search=ttk.Combobox(Detail_Frame,state='readonly',font = ("times new roman", 12,"bold"))
        combo_search['values']=('Name','Class','Gender','Contact')
        combo_search.grid(row=0,column=1, pady=10, padx=20, sticky="w")



        txt_Search = Entry(Detail_Frame ,width=15,relief = GROOVE ,bg="white", font = ("times new roman", 14,"bold"))
        txt_Search.grid(row=0,column=2, pady=10, padx=20, sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10).grid(row=0,column=3,padx=10,pady=10)
        searchbtn=Button(Detail_Frame,text="Show All",width=10).grid(row=0,column=4,padx=10,pady=10)
         #Manage Frame
        Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="blue")
        Table_Frame.place(x=10,y=70,width=760,height=480)


        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)


        Student_table=ttk.Treeview(Table_Frame,columns=("Roll No","Name","Class","Section","Gaurdian","Contact No","Address","DOB"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)

        Student_table.heading("Roll No",text="Roll No")
        Student_table.heading("Name",text="Name")
        Student_table.heading("Class",text="Class")
        Student_table.heading("Section",text="Section")
        Student_table.heading("Gaurdian",text="Gaurdian")
        Student_table.heading("Contact No",text="Contact No")
        Student_table.heading("Address",text="Address")
        Student_table.heading("DOB",text="DOB")


        Student_table['show']='headings'
        Student_table.column("Roll No",width=100)
        Student_table.column("Name",width=100)
        Student_table.column("Class",width=100)
        Student_table.column("Section",width=100)
        Student_table.column("Contact No",width=100)
        Student_table.column("Address",width=150)
        Student_table.column("DOB",width=150)



        Student_table.pack(fill=BOTH,expand=1)
    def add_student(self):
        con= pymysql.connect(host="localhost","root",password="",database="stm")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.rollNoVar.get(),self.addressVar.get(),self.classVar.get(),self.contactVar.get(),self.dobVar.get().self.sectionVar.get())











root =  Toplevel()
ob = Student(root)
root.mainloop()
