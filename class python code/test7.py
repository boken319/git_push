def notepad():
    notes = []
    while True:
        print("\n1. 添加备忘")
        print("2. 查看备忘")
        print("3. 删除备忘")
        print("4. 退出")
        choice = input("选择操作: ")

        if choice == '1':
            note = input("输入你的备忘: ")
            notes.append(note)
            print("备忘已添加！")
        elif choice == '2':
            print("当前备忘:")
            for idx, note in enumerate(notes):
                print(f"{idx + 1}. {note}")
        elif choice == '3':
            note_number = int(input("输入要删除的备忘编号: ")) - 1
            if 0 <= note_number < len(notes):
                notes.pop(note_number)
                print("备忘已删除！")
            else:
                print("无效的编号")
        elif choice == '4':
            break
        else:
            print("无效选择，请重新输入")

notepad()