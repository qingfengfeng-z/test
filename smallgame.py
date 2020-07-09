print('做个小游戏叭')
while True:
    number=input('请输入一个数字')
    guess=int(number)
    if guess==8:
        print('猜对了')
        break
    else:
        if guess<8:
            print('小了小了')
        else:
            print('大了大了')
print('游戏结束')
