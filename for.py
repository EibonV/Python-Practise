#列表For语句
magicians=['爱丽丝','大卫','凯洛玲']
for magician in magicians:
    print(magician)
    print(f"I can't wait to see your next trick,{magician.title()}!\n")
#创建1~4数字
for value in range(1,5):
    print(value)
#创建1~5列表
numbers=list(range(1,6))
print(numbers)
#创建1~10偶数列表
even_numbers=list(range(2,11,2)) 
print(even_numbers)
#创建1~10指数列表
squares=[]
for value in range(1,10):
	square=value**2
	squares.append(square)

print(squares)	
