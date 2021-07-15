#8-3
def make_shirt(size,tip):
    print(f"\nT恤尺寸为{size.title()}")
    print(f"T恤的字样为{tip}")

make_shirt('large','自由赛高！')
make_shirt(size='large',tip='自由赛高！')

#8-4
def make_shirt2(size,tip='I love python'):
    """默认值"""
    print(f"\nT恤的尺寸为{size.title()}")
    print(f"T恤的字样为{tip}")

make_shirt2('large')
make_shirt2('medium')
make_shirt2('large',tip='自由赛高！')

#8-5
def describe_city(name,country='england'):
    print(f"\n{name.title()}来自于{country.title()}")

name=''
info=''
while True:
    if info=='yes':
        break
    name=input('你的名字：')
    country=input('来自国家：')
    if country == '':
        country='england'
    describe_city(name,country)    
    info=input('是否停止？')
