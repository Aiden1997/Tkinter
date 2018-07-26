import tkinter as tk

window = tk.Tk()
window.title('Choice')
window.geometry('1080x720')

var = tk.StringVar()

l = tk.Label(window,textvariable=var,bg='yellow',font=('Arial',12),
        width=15,height=2)
l.pack()

on_click = False
def click_me():
	global on_click
	if on_click == False:
		on_click = True
		var.set('Choice')
	else:
		on_click = False
		var.set('')

b = tk.Button(window,text='click',width=15,height=2,command=click_me)
b.pack()
window.mainloop()

