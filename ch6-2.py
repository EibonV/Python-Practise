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

#6-8
#新建列表
pets = []

#新建宠物信息并储存到pets
pet = { 
    'animal type': 'python', 
    'name': 'john', 
    'owner': 'guido', 
    'weight': '43', 
    'eats': 'bugs' 
    }
pets.append(pet)

pet = {
    'animal type': 'chicken', 
    'name': 'clarence', 
    'owner': 'tiffany', 
    'weight': '2', 
    'eats': 'seeds' 
    }
pets.append(pet)

pet = { 
    'animal type': 'dog', 
    'name': 'peso', 
    'owner': 'eric', 
    'weight': '37', 
    'eats': 'shoes' 
    }
pets.append(pet)

#遍历列表，把宠物信息打出来
for info in pets:
    print(f"\n{info['name'].title()} is a {info['animal type']},{info['weight']} kilometers,it's {info['owner'].title()}'s,it eats {info['eats']}.")
for info in pets:
    print(f"\nHere is about {info['name'].title()}:")
    for key,value in info.items():
        print(f"\t{key}:{value}")

#6-9
#创建字典favorite_places
favorite_places = { 
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'], 
    'erin': ['hawaii', 'iceland'], 
    'willie': ['mt. verstovia', 'the playground', 'new hampshire'] 
    }
for name,places in favorite_places.items():
    print(f"\n{name} like these places:")
    for place in places:
        print(f"\n- {place}")