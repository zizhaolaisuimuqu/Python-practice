import tkinter as gui

window = gui.Tk()
window.title('身份证归属地离线查询v0.0')
window.geometry('500x500')

# 标签
label = gui.Label(window, text='OMG', bg='yellow', font=('Arial', 12), width=10)
label.grid(row=0, column=0)

# 输入框
entry = gui.Entry(window,font=('Arial', 12), width=20)
entry.grid(row=0, column=1)

# 按钮
button = gui.Button(window, text="爆炸", font=('Arial', 12), fg="blue", width=10)
button.grid(row=0, column=2)






from PIL import ImageTk, Image

root = gui.Tk()
#背景
canvas = gui.Canvas(root, width=1200,height=699,bd=0, highlightthickness=0)
imgpath = 'background.gif'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
 
canvas.create_image(700, 500, image=photo)
canvas.pack()
entry=gui.Entry(root,insertbackground='blue', highlightthickness =2)
entry.pack()
 
canvas.create_window(100, 50, width=100, height=20, window=entry)






# 刷新循环
window.mainloop()