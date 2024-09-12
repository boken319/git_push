import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    print("猜一个1到100之间的数字")

    while True:
        guess = int(input("输入你的猜测: "))
        attempts += 1

        if guess < number:
            print("太小了!")
        elif guess > number:
            print("太大了!")
        else:
            print(f"恭喜你，猜对了！总共猜了 {attempts} 次。")
            break
guess_number()