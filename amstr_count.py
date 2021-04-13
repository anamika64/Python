l = []
for i in range(100,1000):
    num = i
    arm = str(i)
    for j in range(len(arm)):
        sum = 0
        a = int(arm[j])
        sum = sum + a**len(arm)
    if sum == num:
        print(num)
        l.append(num)

lenth = len(l)
print(lenth)
