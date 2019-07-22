answer = 78
while True:
    num = int(input("请输入一个1-100的数字:"))
    if num > answer:
        print("太大了啊！")
    elif num < answer:
        print("太小了啊！")
    else:
        print("bingo!")
        break