# 返回前十七位运算出来的验证码
def CalcIDVerifyNumber(number):
    number = number.replace(" ", "")
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
    verifyCodeResult = verifyCode[sum % 11]
    return verifyCodeResult


# 校对验证码和最后一位，成功返回1，不成功返回0
def IsIDNumber(number):
    number = number.replace(" ", "")
    if len(number) != 18:
        return 0
    number = number.upper()
    calcNumber = number[:17]
    verifyNumber = number[17:]
    if verifyNumber == CalcIDVerifyNumber(calcNumber):
        return 1
    return 0


inputNumber = input("Input: ")
print(CalcIDVerifyNumber(inputNumber))
print(IsIDNumber(inputNumber))
