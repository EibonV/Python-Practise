#6-11
#创建名为cities的字典
cities = { 
    'santiago': { 
        'country': 'chile', 
        'population': '6_310_000', 
        'nearby mountains': 'andes' 
        },
    'talkeetna': { 
        'country': 'united states', 
        'population': '876', 
        'nearby mountains': 'alaska range'
        },
   'kathmandu': { 
       'country': 'nepal', 
       'population': '975_453', 
       'nearby mountains': 'himilaya' 
       } 
    } 
#输出相关信息
for name,info in cities.items():
    country = info['country'].title()
    population = info['population']
    mountains = info['nearby mountains'].title()

    print(f"\n{name} is in {country}.")
    print(f"\nIt has a population of about {population}.")
    print(f"\nThe {mountains} mounats are nearby.")