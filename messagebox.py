import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Choice')
window.geometry('1080x720')

def hitme():
	#tk.messagebox.showinfo(title='Hi',message='hhh')
	#tk.messagebox.showwarning(title='Hi',message='nonono')
	#tk.messagebox.showerror(title='Hi',message='error')
	#print(tk.messagebox.askquestion(title='Hi',message='what?'))
    #print(tk.messagebox.askyesno(title='Hi',message='what?'))
    print(tk.messagebox.askokcancel(title='Hi',message='what?'))
tk.Button(window,text='hit me',command=hitme).pack()

window.mainloop()
