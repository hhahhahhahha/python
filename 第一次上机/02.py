money = eval(input("请输入要兑换的钱的金额:"))
s = input("请输入A（美元）或者C（人名币）选择金钱的类型:")

if s in ['a','A']:
    C = money*6
    print("{:.2f}美元兑换{:.2f}人名币".format(money,C))
elif s in ['c','C']:
    A = money/6
    print("{:.2f}人名币兑换{:.2f}美元".format(money,A))