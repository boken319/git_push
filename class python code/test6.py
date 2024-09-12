import random
def rock_paper_scissors():
    choices = ['石头', '剪刀', '布']
    while True:
        computer_choice = random.choice(choices)
        user_choice = input("选择: 石头, 剪刀, 布 (或输入'退出'来结束游戏): ")
        # 检查用户是否选择退出
        if user_choice.lower() == '退出':
            print("游戏结束，谢谢参与！")
            break
            # 检查用户输入是否有效
        if user_choice not in choices:
            print("无效输入，请输入'石头', '剪刀', 或 '布'。")
            continue
            # 比较用户和计算机的选择
        if user_choice == computer_choice:
            print(f"平局！都选择了{user_choice}")
        elif (user_choice == '石头' and computer_choice == '剪刀') or \
                (user_choice == '剪刀' and computer_choice == '布') or \
                (user_choice == '布' and computer_choice == '石头'):
            print(f"你赢了！{user_choice}打败了{computer_choice}")
        else:
            print(f"你输了！{computer_choice}打败了{user_choice}")

        # 调用示例
rock_paper_scissors()