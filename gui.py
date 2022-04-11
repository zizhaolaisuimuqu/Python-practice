import tkinter as gui

window = gui.Tk()
window.title('身份证归属地离线查询v0.0')
window.geometry('500x500')

# 标签
label = gui.Label(window, text='请输入十八位身份证号码', font=('Arial', 12), width=20)
label.grid(row=0, column=0)

# 输入框
id_collect = gui.Entry(window,font=('Arial', 12), width=20)
id_collect.grid(row=0, column=1)


def verify_id(id):
    #通过前十七位生成校验码（计算出的）
    id = id_collect
    number = id.replace(" ", "")
    if number == "":
        return "null"
    if len(number) == 18:
        number = number[:17]
    if len(number) != 17:
        return "error"
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    verifyCode = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
    numberLetter = list(number)
    sum = 0
    for index in range(len(numberLetter)):
        sum += int(numberLetter[index]) * weight[index]
    global verifyCodeResult
    verifyCodeResult = verifyCode[sum % 11]

    # 用计算出的校验码验证最后一位，一样则输出1，不一样则输出0
    number = id.replace(" ", "")
    if len(number) != 18:
        return 0
    number = number.upper()
    verifyNumber = number[17:]
    if verifyNumber == verifyCodeResult:
        return 1
    return 0

    
# 按钮
button = gui.Button(window, text="查询", font=('Arial', 12), fg="blue", width=10, command=verify_id)
button.grid(row=0, column=2)


# 标签
label_verifyCodeResult = gui.Label(window, text='verifyCodeResult', bg='yellow', font=('Arial', 12), width=15)
label_verifyCodeResult.grid()





'''
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
'''











# 刷新循环
window.mainloop()