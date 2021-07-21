#9-1
class Restaurant:
    """创建类Restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        """初始化两个属性：名称和种类"""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """方法1：餐馆提供某食品"""
        print(f"\n{self.name}提供{self.type}!")

    def open_restaurant(self):
        """方法2：餐馆开门了"""
        print(f" {self.name}已经开门了!")

restaurant = Restaurant('皇后','煎饼')
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2
restaurant1 = Restaurant('士兵','披萨')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('小混混','啤酒')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('国王','花卷')
restaurant3.describe_restaurant()