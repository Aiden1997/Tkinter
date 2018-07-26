
import tkinter as tk

window = tk.Tk()
window.title('Choice')
window.geometry('1080x720')

tk.Label(window,text='window').pack()

frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l,text='left1').pack()
tk.Label(frm_l,text='left2').pack()
tk.Label(frm_r,text='right1').pack()

window.mainloop()
