#资源导入部分
from msilib.schema import tables

#函数定义部分
def separate(id_17):
    a = len(str(id_17))
    global id_17_list
    id_17_list = []
    while(a > 0):
        id_17_list.append(id_17 % 10)
        id_17 = id_17 // 10
        a -= 1
    id_17_list.reverse()
    #print('id_17_list:', id_17_list)

def verify_coefficient():
    verify_coefficient = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    a = 1
    while(a <= 17):
        id_17_list.insert(a-1,(verify_coefficient[a-1] * id_17_list.pop(a-1)))
        #id_17_list[a-1] = (verify_coefficient[a-1] * id_17_list.pop(a-1))  //doesn't work
        a += 1
    #print('new id_17_list:', id_17_list)

def verify_code():
    global verify_code
    verify_code = verify_code_list[remainder_list.index(remainder)]
    #print('verify_code:', verify_code)

#接下来是程序主体
id_all = str(input("Enter the id number pleace:"))
#身份证18位判定部分
if len(id_all) != 18:
    print('你再瞎几把乱输我就要报警啦！！！😒')
    quit()
if id_all[0] == 0:
    print('你再瞎几把乱输我就要报警啦！！！😒')
    quit()
if id_all[-1] == 'x':
    id_18 = 10
elif id_all[-1] == 'X':
    id_18 = 10
else:
    id_18 = (int(id_all)) % 10
#print('id_18:', id_18)

#列表生成部分
remainder_list = []
for i in range(0,11):
    remainder_list.append(i)
verify_code_list = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2]

#信息处理部分
id_17 = (int(id_all.rstrip(id_all[-1])))
separate(id_17)
verify_coefficient()
sum = sum(id_17_list)
remainder = sum % 11
verify_code()

#验证部分
if id_18 == verify_code:
    print('verification succeeded')
else:
    print('verification failed')