#习题9-3
class User:
    """创建类User"""
    def __init__(self,first_name,last_name,user_name,email,location):
       """初始化用户属性""" 
       self.fname = first_name
       self.lname = last_name
       self.uname = user_name
       self.email = email
       self.location = location

    def describe_user(self):
        """创建显示用户信息方法"""
        print(f"\n用户名{self.uname}：")
        print(f"\n真实姓名 - {self.fname} {self.lname}")
        print(f"\n注册邮箱 - {self.email}")
        print(f"\n居住地址 - {self.location}")

    def greet_user(self):
        """创建登录欢迎方法"""
        print(f"\n{self.uname}!欢迎回来！")

usermike = User('麦','克','mike','1111@qq.com','北京')
usermike.describe_user()
usermike.greet_user()       