#7-1
car = input("What kind of car do you want?: ")
print(f"\nLet me see if I can find you a {car.title()}")

#7-2
num = input("今天几位就餐？\n")
if int(num) > 8:
    print("没有空桌！")
else:
    print("有空桌！")

#7-3
promot = "输入一个数："
promot += "\n"
numstr = input(promot)
num = int(numstr)
if num%10 == 0:
    print("此数是10的整数倍！")
else:
    print("此数不是10的整数倍！")   