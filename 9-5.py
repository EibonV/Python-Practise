#习题9-5
class User():
    def __init__(self,name,first_name,last_name,email,location):
        """初始化用户信息"""
        self.name = name
        self.fname = first_name
        self.lname = last_name
        self.email = email
        self.location = location
        self.login_attempt = 0

    def describe_user(self):
        """显示用户信息摘要"""
        print(f"\n用户名：{self.name}")
        print(f"\n用户真实姓名：{self.fname} {self.lname}")
        print(f"\n注册邮箱：{self.email}")
        print(f"\n该用户来自:{self.location}")

    def greeting_user(self):
        """显示问候语"""
        print(f"\n欢迎回来 {self.name}!")

    def login_attempts(self):
        """将login_attempt加1"""
        self.login_attempt += 1
        return self.login_attempt

    def login_reset(self):
        """重置login_attempt"""
        self.login_attempt = 0
        return self.login_attempt

    

user = User('mike','麦','克','111@qq.com','北京')

user.describe_user() #显示用户基本信息

user.greeting_user() #显示问候语

num = user.login_attempts() #第一次登陆
print(f"\n{user.name}第{num}次登陆！")

num = user.login_attempts() #第二次登陆
print(f"\n{user.name}第{num}次登陆！")

num = user.login_reset() #重置登陆次数
print(f"\n登陆次数已清{num}!")

