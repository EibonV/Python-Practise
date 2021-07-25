#习题9-4
class Restaurant:
    def __init__(self,name,cuisine_type):
        """初始化餐馆信息"""
        self.name = name
        self.type = cuisine_type
        self.served = 0

    def describe_restaurant(self):
        """显示餐馆信息概要"""
        print(f"\n{self.name}供应美食 {self.type}")

    def open_restaurant(self):
        """显示餐馆营业状态"""
        print(f"\n{self.name}正在营业中！")

    def served_restaurant(self,number_served):
        """设置就餐人数"""
        self.served =  number_served
        return self.served

    def addition_restaurant(self,number_addition):
        """增加就餐人数"""
        self.served += number_addition
        return self.served

restaurant = Restaurant('皇后','披萨')

restaurant.describe_restaurant() #打印餐馆信息摘要

restaurant.open_restaurant() #打印餐馆营业状态

num = restaurant.served_restaurant(100) #设定今日就餐人数
print(f"\n今日就餐人数共{num}人！")

num = restaurant.addition_restaurant(50) #增加50人
print(f"\n今日就餐人数共{num}人！")