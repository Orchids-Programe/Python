from tkinter import *
from random import randint
from tkinter import messagebox
from tkinter import scrolledtext


window = Tk()
window.title('Wellcome to Omachii App')
window.geometry('600x500')

def showon():
    # list = ["Chào mừng tới app của Vũ Long", "Game Ez","Demo GUIDE with Tkinter in Python"]
    name = str(txt1.get())
    passwrd = txt2.get()
    # a = 'Ban chưa nhập đầy đủ thông tin'
    # b = 'Bạn nhập sai thông tin tài khoản'
    if(name == "VuLong" and passwrd == '123456'):
        return showpage2()#list[randint(0,2)]
        # messagebox.showinfo(list[randint(0,1)])
    elif(name== "" or passwrd==""):
        # return a
        messagebox.showinfo('Message Error','Ban chưa nhập đầy đủ thông tin')
    else:
        # return b
        messagebox.showinfo('Message Error','Bạn nhập sai thông tin tài khoản')

# def show():
#     sh = showon()
#     show1 = Text(window, height = 10, width = 30)
#     show1.grid(column = 3, row = 20)
#     show1.insert(END, sh)

def page2():
    window2 = Tk()
    window2.title('My App page 2')
    window2.geometry('800x500')

    label1 = Label(window2, text = 'Quản Lý Khách Hàng')
    label1.grid(column = 0, row = 0)
    label2 = Label(window2, text = 'User Nhân Viên')
    label2.grid(column = 0, row = 1)

    label3 = Label(window2, text = 'Name Customer: ')
    label3.grid(column = 1, row = 1)
    entry1 = Entry(window2, width = '30',bd = 5)
    entry1.grid(column = 3, row =  1)

    label4 = Label(window2, text = 'Identity ID:')
    label4.grid(column = 1, row = 2)
    entry2 = Entry(window2, width = 30, bd = 5)
    entry2.grid(column = 3, row = 2)

    label5 = Label(window2, text = 'Phone Number: ')
    label5.grid(column = 1, row = 3)
    entry3 = Entry(window2, width = 30, bd = 5)
    entry3.grid(column = 3, row = 3)

    label6 = Label(window2, text = 'Address : ')
    label6.grid(column = 1, row = 4)
    entry4 = Entry(window2, width = 30, bd = 5)
    entry4.grid(column = 3, row = 4)

    button = Button(window2, text = 'Add Customer', width = 12, bd = 5)
    button.grid(column = 4, row = 1)
    button1 = Button(window2, text = 'Search Customer', width = 12, bd = 5)
    button1.grid(column = 4, row = 2)
    button2 = Button(window2, text = 'Delete Customer', width = 12, bd = 5)
    button2.grid(column = 4, row = 3)
    button3 = Button(window2, text = 'Cancel', width = 12,bg = 'yellow',fg = 'red', bd = 5, command = window2.destroy)
    button3.grid(column = 4, row = 4)
    text = Text(window2, width = 50, height = 50)
    text.grid(column = 4, row = 6)

    window2.mainloop()

def showpage2():
    gre = page2()
    gre.tkraise()

label1 = Label(window, text = 'Have a good day')
label1.grid(column= 0, row = 0)

label2 = Label(window, text = 'Chăm chỉ, Tìm tòi, Không ngại khó')
label2.grid(column = 0, row = 1)

label3 = Label(window, text = 'UserName')
label3.grid(column = 2, row = 4)
txt1 = Entry(window, width = 30, bd = 5)
txt1.grid(column = 3, row = 4)

label4 = Label(window, text = " PassWord")
label4.grid(column = 2, row = 5)
txt2 = Entry(window, width = 30,bd = 5,show = '*')
txt2.grid(column = 3, row = 5)

btn1 = Button(window, text = 'Sign In',bd = 4, fg = 'Green', width = 10, command = showon)
btn1.grid(column = 2, row = 7)
label5 = Label(window, text = 'Forgot PassWord?')
label5.grid(column = 2, row = 6)
btn2 = Button(window, text = 'Cancel', bd = 4, fg = "Red", bg = "Yellow", width = 10, command = window.destroy)
btn2.grid(column = 3, row = 7)

checkbutton = Checkbutton(window, text = "I'm Not Robot")
checkbutton.grid(column = 2, row = 11)

#chen thanh cuon
#toa do thanh cuon
# sb1 = Scrollbar(window)
# sb1.grid(column = 10, row = 0, rowspan = 10)
# txt = scrolledtext.ScrolledText(window, width = 0, height = 0)
# txt.grid(column = 10, row = 0)

window.mainloop()