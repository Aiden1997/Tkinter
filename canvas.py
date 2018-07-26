import tkinter as tk

window = tk.Tk()
window.title('Choice')
window.geometry('1080x720')

canvas = tk.Canvas(window,bg='white',height=600,width=600)
image_file = tk.PhotoImage(file='tri.gif')
image = canvas.create_image(500,300,anchor='se',image=image_file)
rect = canvas.create_rectangle(550,30,580,50)

canvas.pack()

def moveit():
	canvas.move(rect,0,2)

b = tk.Button(window,text='move',command=moveit).pack()


window.mainloop()
