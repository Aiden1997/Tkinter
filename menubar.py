
import tkinter as tk

window = tk.Tk()
window.title('Choice')
window.geometry('1080x720')

l = tk.Label(window,text='',bg='yellow')
l.pack()

count = 0
def do_job():
	global count
	l.config(text='do '+ str(count))
	count += 1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

submenu = tk.Menu(filemenu,tearoff=0)
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
submenu.add_command(label='Submenu1',command=do_job)
window.config(menu=menubar)

window.mainloop()
