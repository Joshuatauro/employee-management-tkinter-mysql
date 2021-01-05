from tkinter import *
import mysql.connector
import tkinter.messagebox
import os
import 
from tkinter import ttk

def clickednum(n):
    sum = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(sum)+str(n))

def clickedsum():
    sum = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(sum) + '+')

def clickedminus():
    sum = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(sum) + '-')

def clickedmultiply():
    sum = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(sum) + 'x')

def clickeddivide():
    sum = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(sum) + '/')

def clickedequal():
    try:
        equation = entry.get()
        for index,check in enumerate(equation):
            if check == '+':
                firstnum = equation[0:index]
                f_num = int(firstnum)
                secondnum = equation[index+1:]
                s_num = int(secondnum)

                output = f_num+s_num
                entry.delete(0,END)
                entry.insert(0,output)

            elif check == 'x':
                firstnum = equation[0:index]
                f_num = int(firstnum)
                secondnum = equation[index+1:]
                s_num = int(secondnum)

                output = f_num*s_num
                entry.delete(0,END)
                entry.insert(0,output)
                
            elif check == '-':
                firstnum = equation[0:index]
                f_num = int(firstnum)
                secondnum = equation[index+1:]
                s_num = int(secondnum)

                output = f_num-s_num
                entry.delete(0,END)
                entry.insert(0,output)
            
            elif check == '/':
                firstnum = equation[0:index]
                f_num = int(firstnum)
                secondnum = equation[index+1:]
                s_num = int(secondnum)

                output = f_num/s_num
                entry.delete(0,END)
                entry.insert(0,int(output))

    except ValueError:
        tkinter.messagebox.showerror('Wrong format' , 'Please enter a correct format')
    except ZeroDivisionError:
        tkinter.messagebox.showerror('Wrong format' , 'Cannot divide by 0')


def clickedclear():
    entry.delete(0,END)

def clickedbackspace():
    equation = entry.get()
    entry.delete(0,END)
    length = len(equation)
    new_str = equation[0:length-1]
    entry.insert(0,new_str)

def insertdb(): 
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "yourpassword",
        database = "yourdatabasename"
    )

    name = e_name_entry.get()
    sal = e_sal_entry.get()
    identity = e_id_entry.get()
    desig = e_desig_entry.get()
    allowance = e_allowance_entry.get()
    username_entered = username_entry.get()

    cursor = mydb.cursor()
    try:
        if (name == '' or sal == '' or identity == '' or desig == ''  or allowance == ''):
            Tk().withdraw()
            tkinter.messagebox.showerror('Details missing' , 'Please enter all the details')
        else:
            cursor.execute("insert into "+ username_entered+" values ('"+ identity + "' , '"+ name + "','" + desig + "' , '" + sal + "' , '" + allowance +"')")
            e_name_entry.delete(0,END)
            e_sal_entry.delete(0,END)
            e_id_entry.delete(0,END)
            e_desig_entry.delete(0,END)
            e_allowance_entry.delete(0,END)
            mydb.commit()

            e_id_entry.insert(0 , int(identity)+1)
            display() 
            tkinter.messagebox.showinfo('Done' , 'Success')
    except mysql.connector.errors.IntegrityError:
        tkinter.messagebox.showerror('Error' , 'Id already in use')

def searchdb():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "yourpassword",
        database = "yourdatabasename"
    )

    identity = e_id_entry.get()
    username_entered = username_entry.get()

    cursor = mydb.cursor()

    if (identity == ''):
        Tk().withdraw()   
        tkinter.messagebox.showerror('Details missing' , 'Please enter the ID')
    else:
        cursor.execute("select * from "+username_entered+" where id = '"+identity+" ' ")
        row = cursor.fetchall()

        for i in row:
            e_name_entry.insert(0 , i[1])
            e_sal_entry.insert(0 , i[3])
            e_desig_entry.insert(0 , i[2])
            e_allowance_entry.insert(0 , i[4])
            display()
            tkinter.messagebox.showinfo('Done' , 'Success')
    

def deletedb():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "yourpassword",
        database = "yourdatabasename"
    )
    try:
        identity = e_id_entry.get()
        username_entered = username_entry.get()
        
        cursor = mydb.cursor()
        if identity == '':
            Tk().withdraw()
            tkinter.messagebox.showerror('Details missing' , 'Enter the employee ID')
        else:
            cursor.execute("delete from "+ username_entered +" where id = '" +identity +"'")

            e_name_entry.delete(0,END)
            e_sal_entry.delete(0,END)
            e_id_entry.delete(0,END)
            e_desig_entry.delete(0,END)
            e_allowance_entry.delete(0,END)
            mydb.commit()
            display()
            tkinter.messagebox.showinfo('Done' , 'Success')
    except _tkinter.TclError:
        pass
        
def updatedb():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "yourpassword",
        database = "yourdatabasename"
    )

    try:
        name = e_name_entry.get()
        sal = e_sal_entry.get()
        identity = e_id_entry.get()
        desig = e_desig_entry.get()
        allowance = e_allowance_entry.get()
        username_entered = username_entry.get()

        cursor = mydb.cursor()
        
        if (name == '' or sal == '' or identity == '' or desig == ''  or allowance == ''):
            tkinter.messagebox.showerror('Details missing' , 'Please enter all the details')
        else:
            cursor.execute("update "+username_entered+" set id = '" + identity + "' ,  name = '" + name + "' , designation = '" + desig +"' ,  salary = '" + sal +"' ,  allowance = '" + allowance +" ' where id = '"+identity+"'")
            mydb.commit()
            e_name_entry.delete(0,END)
            e_sal_entry.delete(0,END)
            e_id_entry.delete(0,END)
            e_desig_entry.delete(0,END)
            e_allowance_entry.delete(0,END)
            mydb.commit()
            display()
            tkinter.messagebox.showinfo('Done' , 'Success')

    except _tkinter.TclError:
        pass

def display():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "yourpassword",
        database = "yourdatabasename"
)
    username_entered = username_entry.get()
    try:
        for i in tv.get_children():
            tv.delete(i)
        cursor = mydb.cursor()
        cursor.execute("select * from " + username_entered)
        rows = cursor.fetchall()

        for i in rows:
            tv.insert('','end',value = i)

    except _tkinter.TclError:
        print('FOUND')

def verify_checker():
    username_entered = username_entry.get()
    password_entered = password_entry.get()
    try:
        file = open(username_entered+'.txt' , 'r')
        for i in file:
            if i == password_entered:
                access = Label(verify , text = '    Access granted' , fg = 'green' , width = 25 , bg = "#17171E")
                access.place(x = 160 , y = 250)
                password_entry.delete(0,END)
                verify.withdraw()
                openapp()
            else:
                wrong = Label(verify , text = 'Wrong username or passwowwrd' , fg = 'red' , bg = "#17171E")
                wrong.place(x = 160 , y = 250)
                password_entry.delete(0,END)
                

    except FileNotFoundError:
        wrong = Label(verify , text = 'Wrong username or password' , fg = 'red' , bg = "#17171E")
        wrong.place(x = 160 , y = 250)
        password_entry.delete(0,END)
    except mysql.connector.errors.ProgrammingError:
        tkinter.messagebox.showerror('Access Denied' , 'Table not found')

def home_return():
    screen.destroy()
    homepage()
                
def openapp(): 
    global screen
    screen = Tk()
    screen.configure(bg ="#0F0F0F")
    screen.title('JoshuaTech | Employee Database')
    screen.geometry('1350x1350')

    global e_name_entry
    global e_id_entry
    global e_desig_entry
    global e_sal_entry
    global e_allowance_entry
    global e_doj_entry
    global tv
    global entry

    
    e_id = Label(screen , text = "Enter employee ID : " , bg = "#0F0F0F" , fg = "white")
    e_id_entry = Entry(screen , width = 55)
    e_id.place(x = 20 , y = 22)
    e_id_entry.place(x = 220 , y = 22)

    e_name = Label(screen , text = "Enter employee name : " , bg = "#0F0F0F" , fg = "white")
    e_name_entry = Entry(screen , width = 55)
    e_name.place(x = 20 , y = 62)
    e_name_entry.place(x = 220 , y = 62)

    e_desig = Label(screen , text = "Enter employee designation : " , bg = "#0F0F0F" , fg = "white")
    e_desig_entry = Entry(screen , width = 55)
    e_desig.place(x = 20 , y = 102)
    e_desig_entry.place(x = 220 , y = 102)

    e_sal = Label(screen , text = "Enter employee salary : " , bg = "#0F0F0F" , fg = "white")
    e_sal_entry = Entry(screen , width = 55)
    e_sal.place(x = 20 , y = 142)
    e_sal_entry.place(x = 220 , y = 142)

    e_allowance = Label(screen , text = "Enter employee allowance : " , bg = "#0F0F0F" , fg = "white")
    e_allowance_entry = Entry(screen , width = 55)
    e_allowance.place(x = 20 , y = 182)
    e_allowance_entry.place(x = 220 , y = 182)

    scrollbar = ttk.Scrollbar()
    
    tv = ttk.Treeview(screen , column = (1,2,3,4,5) , show = 'headings' , height = 13)
    tv.heading(1 , text = 'ID')
    tv.heading(2 , text = 'NAME')
    tv.heading(3 , text = 'DESIGNATION')
    tv.heading(4 , text = 'SALARY')
    tv.heading(5 , text = 'ALLOWANCE')

    scrollbar.configure(command = tv.yview)
    tv.configure(yscrollcommand = tv.set)

    tv.place(x = 95 , y = 333)

    display() 

    

    create = Button(screen , text = "Add new details" , command = insertdb)
    search = Button(screen , text = "Search with e_id" , command = searchdb)
    update = Button(screen , text = "Update details with e_id" , command = updatedb)
    delete = Button(screen , text = "Delete details using e_id" , command = deletedb)


    create.place(x = 20 , y = 230)
    search.place(x = 130 , y = 230)
    update.place(x = 240 , y = 230)
    delete.place(x = 395 , y = 230)

    
    entry = Entry(screen , width = 44)

    b_0 = Button(screen , text = '0' , width = 27 , height = 3 , bg = 'black' , fg = 'white' , activebackground = '#19191a' , relief = 'groove' , bd = 5 , command = lambda:clickednum(0))
    b_1 = Button(screen , text = '1' , width = 8 , height = 3 , bg = 'black' , fg = 'white' , activebackground = '#19191a' , relief = 'groove' , bd = 5 ,  command = lambda:clickednum(1))
    b_2 = Button(screen , text = '2' , width = 8 , height = 3 , bg = 'black' , fg = 'white' , activebackground = '#19191a' , relief = 'groove' , bd = 5 ,  command = lambda:clickednum(2))
    b_3 = Button(screen , text = '3' , width = 8 , height = 3 , bg = 'black' , fg = 'white' , activebackground = '#19191a' , relief = 'groove' , bd = 5 ,  command = lambda:clickednum(3))
    b_4 = Button(screen , text = '4' , width = 8 , height = 3 , bg = 'black' , fg = 'white' , activebackground = '#19191a' , relief = 'groove' , bd = 5 ,  command = lambda:clickednum(4))
    b_5 = Button(screen , text = '5' , width = 8 , height = 3 , bg = 'black' , fg = 'white' , activebackground = '#19191a' , relief = 'groove' , bd = 5 ,  command = lambda:clickednum(5))
    b_6 = Button(screen , text = '6' , width = 8 , height = 3 , bg = 'black' , fg = 'white' , activebackground = '#19191a' ,relief = 'groove' , bd = 5 ,  command = lambda:clickednum(6))
    b_7 = Button(screen , text = '7' , width = 8 , height = 3 , bg = 'black' , fg = 'white' , activebackground = '#19191a' , relief = 'groove' , bd = 5 ,  command = lambda:clickednum(7))
    b_8 = Button(screen , text = '8' , width = 8 , height = 3 , bg = 'black' , fg = 'white' , activebackground = '#19191a' , relief = 'groove' , bd = 5 ,  command = lambda:clickednum(8))
    b_9 = Button(screen , text = '9' , width = 8 , height = 3 , bg = 'black' , fg = 'white' , activebackground = '#19191a' , relief = 'groove' , bd = 5 ,  command = lambda:clickednum(9))

    b_equal = Button(screen , text = '=' , width = 18 , height = 3 , bg = 'black' , fg = '#fa4002' , activebackground = '#19191a' ,  activeforeground = '#fa4002' , relief = 'groove' , bd = 5 ,  command = clickedequal)
    b_plus = Button(screen , text = '+' , width = 8 , height = 3 , bg = 'black' , fg = '#fa4002' , activebackground = '#19191a' , activeforeground = '#fa4002' , relief = 'groove' , bd = 5 ,  command = clickedsum)
    b_minus = Button(screen , text = '-' , width = 8 , height = 3 , bg = 'black' , fg = '#fa4002' , activebackground = '#19191a' , activeforeground = '#fa4002' , relief = 'groove' , bd = 5 ,  command = clickedminus)
    b_divide = Button(screen , text = '/' , width = 8 , height = 3 , bg = 'black' , fg = '#fa4002' , activebackground = '#19191a' , activeforeground = '#fa4002' , relief = 'groove' , bd = 5 , command = clickeddivide)
    b_multiply = Button(screen , text = 'x' , width = 8 , height = 3 , bg = 'black' , fg = '#fa4002' , activebackground = '#19191a' , activeforeground = '#fa4002' , relief = 'groove' , bd = 5 ,  command = clickedmultiply)
    b_clear = Button(screen , text = 'C' , width = 8 , height = 3 , bg = 'black' , fg = '#fa4002' , activebackground = '#19191a' , activeforeground = '#fa4002' , relief = 'groove' ,  bd = 5 , command = clickedclear)
    b_backspace = Button(screen , text = 'Backspace' , width = 8 , height = 3 , bg = 'black' , fg = '#fa4002' , activebackground = '#19191a' , activeforeground = '#fa4002' , relief = 'groove' , bd = 5 ,  command = clickedbackspace)  

    b_0.place(x = 800 , y = 265)
    b_1.place(x = 800 , y = 209)
    b_2.place(x = 866 , y = 209)
    b_3.place(x = 932 , y = 209)
    b_4.place(x = 800 , y = 153)
    b_5.place(x = 866 , y = 153)
    b_6.place(x = 932 , y = 153)
    b_7.place(x = 800 , y = 97)
    b_8.place(x = 866 , y = 97)
    b_9.place(x = 932 , y = 97)
    

    b_equal.place(x = 800 , y = 41)
    b_plus.place(x = 999 , y = 265)
    b_minus.place(x = 999 , y = 209)
    b_divide.place(x = 999 , y = 153)
    b_multiply.place(x = 999 , y = 97)
    b_clear.place(x = 933 , y = 41)
    b_backspace.place(x = 999 , y = 41)

    entry.place(x = 800 , y = 22)

def showpass():
    global count
    count += 1
    if count % 2 == 0:
        password_entry.configure(show = '')
    else:
        password_entry.configure(show = '*')
    
def showpass_reg():
    global count_reg
    count_reg += 1
    if count_reg % 2 == 0:
        reg_pass_entry.configure(show = '')
    else:
        reg_pass_entry.configure(show = '*')
    

def verification():
    global username_entry
    global password_entry
    global verify
    global count

    homepage.destroy()
    
    verify = Tk()
    verify.configure(bg = "#17171E")
    verify.geometry('500x300')
    verify.title('JoshuaTech | Verification')
    
    username = Label(verify , text = 'Enter username' , bg = '#17171E' , fg = 'white')
    username.place(x = 50 , y = 90)
    username_entry = Entry(verify , width = 20)
    username_entry.place(x = 160 , y = 90)
    
    password = Label(verify , text = 'Password' , bg = '#17171E' , fg = 'white')

    password_entry = Entry(verify)
    password_entry.configure(show = '*')


    count = 0
    show_pass = Button(verify , text = 'show' , command = showpass).place(x = 290 , y = 130)
    
    
    password.place(x = 55 , y = 130)
    password_entry.place(x = 160 , y = 130)
    
    submit = Button(verify , text = 'Submit' , command = verify_checker)
    submit.place(x = 150 , y = 210 , width = 100)

def register_user(): 
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "yourpassword",
        database = 'joshuatech'
)

    Tk().withdraw()
    username_reg = reg_username_entry.get()
    pass_reg = reg_pass_entry.get()
    
    cursor = mydb.cursor()
    try:
        if (username_reg == '' or pass_reg == ''):
            #Tk.withdraw()
            tkinter.messagebox.showerror('Missing details','Please enter all details')
        else:
            if os.path.isfile(username_reg+'.txt') is False:
                file = open(username_reg+'.txt' , 'w')
                file.write(pass_reg)
                register.destroy()
                cursor.execute( "CREATE TABLE "+ username_reg + " ( id INT(20) PRIMARY KEY , name CHAR(200) , designation CHAR(200) , salary INT(200) , allowance INT(200))")
                tkinter.messagebox.showinfo('Success' , 'Account Registered')
                mydb.commit()
            else:
                tkinter.messagebox.showerror('Error' , 'Username in use')

    except mysql.connector.errors.ProgrammingError:
        tkinter.messagebox.showerror('Error' , 'Username in use')

def registration():
    global reg_username_entry
    global reg_pass_entry
    global register
    global count_reg

    register = Tk()
    register.geometry('500x300')
    register.configure(bg = '#17171E')
    register.title('JoshuaTech | Registration')

    reg_username = Label(register , text = 'Username').place(x = 20 , y = 20)
    reg_username_entry = Entry(register)
    reg_username_entry.place(x = 120 , y = 20)

    reg_pass = Label(register , text = 'Password').place(x = 20 , y = 60)
    reg_pass_entry = Entry(register)
    reg_pass_entry.place(x = 120 , y = 60)
    reg_pass_entry.configure(show = '*')

    count_reg = 0
    reg_show_button = Button(register , text = 'show' , command = showpass_reg).place(x = 250 , y = 60)

    
    register_button = Button(register , text = 'Register' , command = register_user).place(x = 70 , y = 140)

def homepage():
    global homepage
    homepage = Tk()
    homepage.configure(bg = "#17171E")
    homepage.geometry('500x300')
    homepage.title('JoshuaTech App')

    home_verification = Button(homepage , text = 'Employee database' , command =  verification , width = 14).place(x = 180 , y = 140)
    home_registration = Button(homepage , text = 'Register' , command = registration , width = 14).place(x = 180 , y = 100)

homepage()



