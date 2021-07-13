#6-7
#6-1原字典
person = {
    'first name':'eric',
    'last name':'mattes',
    'age':'43',
    'city':'sitka'
    }
#创建2个新字典
person2 = {
    'first name':'james',
    'last name':'bander',
    'age':'51',
    'city':'london'
}
person3 = {
    'first name':'trumple',
    'last name':'brun',
    'age':'60',
    'city':'newyourk'
}
#创建字典列表
people = [person,person2,person3]
for info in people:
    print(f"\n{info['first name'].title()} {info['last name'].title()} is {info['age']} years old,living in {info['city'].title()} city")
