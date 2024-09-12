def calculator():
    print("欢迎使用简易计算器")

    num1 = float(input("输入第一个数字: "))
    operation = input("选择操作 (+, -, *, /): ")
    num2 = float(input("输入第二个数字: "))

    if operation == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("除数不能为零！")
    else:
        print("无效操作")

calculator()