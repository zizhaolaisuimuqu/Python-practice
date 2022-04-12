import tkinter as gui


#通过前十七位生成校验码（计算出的）
def verify():
    id = id_entry.get()
    number = str(id)
    number = number.replace(" ", "")

    loopnumber = 1
    
    # 数值显示的擦除
    text_verifystate.delete(1.0, "end")
    text_caculateCode.delete(1.0, "end")
    text_directCode.delete(1.0, "end")
    text_verifyresult.delete(1.0, "end")


    if len(number) == 18:
        number = number[:17]
    else:
        text_verifystate.delete(1.0, "end")
        text_verifystate.insert("end","失败，因为身份证格式错误")
        loopnumber = 0
    if number == "":
        text_verifystate.delete(1.0, "end")
        text_verifystate.insert("end","失败，因为输入值为空")
        loopnumber = 0


    while loopnumber == 1:
        loopnumber = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        verifyCode = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
        numberLetter = list(number)
        sum = 0
        for index in range(len(numberLetter)):
            sum += int(numberLetter[index]) * weight[index]
        global caculateCode
        caculateCode = verifyCode[sum % 11]

        # 用计算出的校验码验证最后一位
        number = id.replace(" ", "")
        number = number.upper()
        directCode = number[17:]
        if directCode == caculateCode:
            verifyresult = '通过'
        else:
            verifyresult = '不通过'
        
        # 数值显示的写入
        text_verifystate.insert("end","完成")
        text_caculateCode.insert("end",caculateCode)
        text_directCode.insert("end",directCode)
        text_verifyresult.insert("end",verifyresult)



# 主窗口
window = gui.Tk()
window.title('身份证归属地离线查询v0.0')
window.geometry('500x500')



# 标签-请输入十八位身份证号码
label = gui.Label(window, text='请输入十八位身份证号码', font=('Arial', 12), width=20)
label.grid(row=0, column=0)
# 身份证号码输入框
id_entry = gui.Entry(window,font=('Arial', 12), width=20)
id_entry.grid(row=0, column=1)
id = id_entry.get()


# 标签-校验状态
label_verifystate = gui.Label(window, text='校验状态', bg='yellow', font=('Arial', 12), width=15)
label_verifystate.grid(row=1, column=0)
# 数值显示-校验状态
text_verifystate = gui.Text(window, font=('Arial', 12), height=1, width=20)
text_verifystate.grid(row=1, column=1)


# 标签-计算校验码
label_caculateCode = gui.Label(window, text='计算校验码', bg='yellow', font=('Arial', 12), width=15)
label_caculateCode.grid(row=2, column=0)
# 数值显示-计算校验码
text_caculateCode = gui.Text(window, font=('Arial', 12), height=1, width=20)
text_caculateCode.grid(row=2, column=1)


# 标签-直接校验码
label_directCode = gui.Label(window, text='直接校验码', bg='yellow', font=('Arial', 12), width=15)
label_directCode.grid(row=3, column=0)
# 数值显示-直接校验码
text_directCode = gui.Text(window, font=('Arial', 12), height=1, width=20)
text_directCode.grid(row=3, column=1)


# 标签-验证结果
label_verifyresult = gui.Label(window, text='验证结果', bg='yellow', font=('Arial', 12), width=15)
label_verifyresult.grid(row=4, column=0)
# 数值显示-校验结果
text_verifyresult = gui.Text(window, font=('Arial', 12), height=1, width=20)
text_verifyresult.grid(row=4, column=1)




# 按钮
button_caculate = gui.Button(window, text="查询", font=('Arial', 12), fg="blue", width=10, command=verify)
button_caculate.grid(row=0, column=2)








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