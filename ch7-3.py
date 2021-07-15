#7-8
#创建列表sandwich_orders
sandwich_orders = ['草莓三明治','火腿三明治','番茄三明治','牛肉三明治','牛肉三明治','牛肉三明治']
#创建空列表finished_sandwiches
finished_sandwiches = []
for sandwiche in sandwich_orders:
    print(f"\n{sandwiche}正在制作！")
    finished_sandwiches.append(sandwiche)

for sandwiche in finished_sandwiches:
    print(f"\n{sandwiche}已完成！")   

#7-9
print("本店的牛肉三明治卖完了！\n")
while '牛肉三明治' in finished_sandwiches:
    finished_sandwiches.remove('牛肉三明治')

for sandwiche in finished_sandwiches:
    print(f"\n{sandwiche}") 

#7-10
promot1 = '你的名字？'
promot2 = '你梦想的度假胜地？'
info = ''
places = {}
while True:
    if info == 'no':
        break
    name = input(promot1)
    place = input(promot2)
    places[name]=place
    info=input("还有谁要接受调查吗？")
print("调查结果如下：")
for name,place in places.items():
    print(f"\n{name}要去{place}度假")    