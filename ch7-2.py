#7-4
promot = "请输入配料：\n"
material = "0"
while material != "quit":
    material = input(promot)
    if material != "quit":
        print(f"\n{material}已添加！")

#7-5
promot = "请输入年龄：\n"
agestr = "0"
while agestr != "quit":
    agestr = input(promot)
    if agestr != "quit":
        age = int(agestr)
        if age < 3:
            print("\n免费！\n")
        elif age < 12:
            print("\n需要10美元！\n")
        else:
            print("\n需要15美元！\n")

#7-6
promot = "请输入年龄：\n"
agestr = "0"
while True:
    agestr = input(promot)
    if agestr == "quit":
        break
    else:
        age = int(agestr)
        if age < 3:
            print("\n免费！\n")
        elif age < 12:
            print("\n需要10美元！\n")
        else:
            print("\n需要15美元！\n")     