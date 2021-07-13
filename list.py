#列表示例
bicycle=['trek','cannondal','redline','specialized']
print(bicycle[1].title())
bicycle.append('ducati') #末尾增加元素'ducati'
print(f"\n\t{bicycle}")
print(bicycle[4].title()) #输出5号位元素，并首字母大写
bicycle.insert(1,'honda') #2号位增加元素'honda'
print(f"\n\t{bicycle}")
del bicycle[1] #删除2号位元素'honda'
print(f"\n\t{bicycle}")
popedbicycle=bicycle.pop() #提取末尾删除项
print(popedbicycle.title()) #显示末尾删除项
print(f"\n\t{bicycle}")
bicycle.append(popedbicycle)
print(f"\n\t{bicycle}")
too_expensive='ducati' #指出需删除字符串
bicycle.remove(too_expensive) #移除字符串
print(f"\n最贵的车是：{too_expensive.title()}") #输出移除的字符串
print(f"\n\t{bicycle}")
bicycle.sort() #正序排列列表
print(f"\n\t{bicycle}")
bicycle.reverse() #倒序排列列表
print(f"\n\t{bicycle}")
sortedlist=sorted(bicycle)
print(f"\n\t临时排序：{sortedlist}")
print(f"\n\t{bicycle}")
print(f"\n列表长度为{len(bicycle)}") #确定列表长度