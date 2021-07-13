#6-1
#创建字典
person = {
    'first name':'eric',
    'last name':'mattes',
    'age':'43',
    'city':'sitka'
    }

#打印字典数据
print(person['first name'])
print(person['last name'])
print(person['city'])
print(person['age'])

#6-2
#创建字典
favorite_num = {
    'Alice':'7',
    'Brown':'88',
    'Bob':'100',
    'Hellen':'99',
    'Lily':'10000'
    } 

for name,num in favorite_num.items():
    print(f"\nIs {num} your favorite number,{name}?")

#6-4
#创建字典
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.', 
    'loop': 'Work through a collection of items, one at a time.', 
    'dictionary': "A collection of key-value pairs."  
    }

#循环
for word,name in glossary.items():
    print(f"\n{word}:{name}")

#新建新字典
glossary2 = {
    'List':'A collection of items in a particular order.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.'
    }

#加入原字典
for word,name in glossary2.items():
    glossary[word] = name

#循环
for word,name in glossary.items():
    print(f"\n{word}:{name}")

#6-5
#创建字典
river = {
    'nile':'egypt',
    'mississippi': 'united states', 
    'fraser': 'canada'
    }

for name,county in river.items():
    print(f"\n{name.title()} is run through {county.title()}")
print("\nThe following are rivers:")
for name in river.keys():
    print(f"\n\t{name.title()}")
print("\nThe following are counties:")
for county in river.values():
    print(f"\n\t{county.title()}")   


#6-6
#字典1：清单中程序员
favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python'
    }

#字典2：所有程序员名单
coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"{coder.title()}!,Thanks for join us!")
    else:
        print(f"{coder.title()}!,may you join us?")
