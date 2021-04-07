import math
dayfactor = 0.01
dayup = math.pow(1.0+dayfactor,365)
daydown = math.pow(1.0-dayfactor,365)

print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))

day = 1.0
for i in range(71):
    day = math.pow(1.0+dayfactor,3)
    day = math.pow(day-dayfactor,2)

print("三天打鱼两天晒网：{:.2f}".format(day))