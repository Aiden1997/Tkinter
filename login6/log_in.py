import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title('Welcome to Choice')
window.geometry('450x300')

#image
canvas = tk.Canvas(window,height=200,width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

#user info
tk.Label(window,text='User name:').place(x=50,y=150)
tk.Label(window,text='Password:').place(x=50,y=190)

var_user_name = tk.StringVar()
var_user_name.set('example@python.com')
entry_name = tk.Entry(window,textvariable=var_user_name)
entry_name.place(x=160,y=150)

var_user_pwd = tk.StringVar()
entry_pwd = tk.Entry(window,textvariable=var_user_pwd,show='*')
entry_pwd.place(x=160,y=190)

#login and sign up button

def login():
    user_name = var_user_name.get()
    user_pwd = var_user_pwd.get()
    # print(user_name)
    # print(user_pwd)                                ok!
    try:
        with open('user_info.pickle','rb') as user_file:
            user_info = pickle.load(user_file)
    except FileNotFoundError:
        with open('user_info.pickle','wb') as user_file:
            user_info = {'admin':'admin'}
            pickle.dump(user_info,user_file)
    if user_name in user_info:
        if user_pwd == user_info[user_name]:
            tk.messagebox.showinfo(title='Welcome',message='Hello,' + user_name +'! How are you?')
        else:
            tk.messagebox.showinfo(title='Alert',message='Wrong password,' + user_name)
    else:
        is_sign_up = tk.messagebox.askyesno(title='Welcome',message='You are new here. Sign up today?')
        if is_sign_up:
            sign_up()



def sign_up():
    def new_user():
        np = new_user_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_user_name.get()
        with open('user_info.pickle','rb') as user_file:
            exist_user_info = pickle.load(user_file)
        if np != npf:
            tk.messagebox.showerror(title='Error',message='Check your password again, please!')
        elif nn in exist_user_info:
            tk.messagebox.showerror(title='Error',message='You have already signed up!')
        else:
            exist_user_info[nn] = np
            with open('user_info.pickle','wb') as user_file:
                pickle.dump(exist_user_info,user_file)
            tk.messagebox.showinfo(title='Welcome',message='Sign up successfully!')
            window_sign_up.destroy()
        
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')
    
    tk.Label(window_sign_up,text='User name:').place(x=10,y=10)
    tk.Label(window_sign_up,text='Password:').place(x=10,y=50)
    tk.Label(window_sign_up,text='Password confirm:').place(x=10,y=90)
    
    new_user_name = tk.StringVar()
    new_user_name.set('example@python.com')
    entry_new_name = tk.Entry(window_sign_up,textvariable=new_user_name)
    entry_new_name.place(x=150,y=10)

    new_user_pwd = tk.StringVar()
    entry_new_pwd = tk.Entry(window_sign_up,textvariable=new_user_pwd,show='*')
    entry_new_pwd.place(x=150,y=50)
    
    new_pwd_confirm = tk.StringVar()
    entry_new_pwd_confirm = tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*')
    entry_new_pwd_confirm.place(x=150,y=90)
    
    button_new = tk.Button(window_sign_up,text='Sign up',command=new_user)
    button_new.place(x=150,y=130)
    

button_login = tk.Button(window,text='Login',command=login)
button_login.place(x=170,y=230)

button_sign_up = tk.Button(window,text='Sign up',command=sign_up)
button_sign_up.place(x=270,y=230)





window.mainloop()
