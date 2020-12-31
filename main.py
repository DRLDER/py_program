# ----------------------------------------------------------------------------------------------------------------------
# This is a test about how to use *attribute to trans many attributes
# ----------------------------------------------------------------------------------------------------------------------
# def fun(*name):
#     if (len(name) >= 3):
#         print(name[2])
#     else:
#         print(name[0])
#
#
# fun('a', 'b')
# fun('a', 'b', 'c')
# ----------------------------------------------------------------------------------------------------------------------
# This is a test about class and function and define a try-except
#
#
# class myclass:
#     name = 'admin'
#     age = 12
#
#     def __init__(self, name=name, age=age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         if self.name.isalpha() and isinstance(self.age, int):
#             return self.name + ", this year is " + str(self.age) + " years old!"
#         else:
#             print("you must write the correct name or age!")
#             return False
#
#
# while 1:
#     name = input('write your name!\n')
#     age = input('write your age!\n')
#     try:
#         a = myclass(name, int(age))
#     except ValueError:
#         print("ERROR: You must line in a int number!")
#     else:
#         print(a.show())
#         break
#
#
# ----------------------------------------------------------------------------------------------------------------------
# This is about how to use father or child class
# ----------------------------------------------------------------------------------------------------------------------
# class Parent:
#     def __init__(self, name):
#         self.parentName = name
#         print("\nthis is a parent class build function show: [" + self.parentName + "].\n")
#
#     def show(self):
#         self.parentName = "parentName:parent"
#         print('\nthis is a parent class function to show: [' + self.parentName + '].\n')
#
#     def showTip(self):
#         self.Tip = "[parent:ShowTip()]"
#         print('\nthis is a parent class function to show: ' + self.Tip + '.\n')
#
#
# class Child(Parent):
#     def __init__(self, name):
#         # Parent.__init__(self,name)
#         self.childName = name
#         print("\nthis is a child class build function show: [" + self.childName + "].\n")
#
#     def show(self):
#         super().show()
#
#
# # a = child('GZJ')
# a = Parent('GZJ')
# a.show()
# b = Child('Polaris')
# b.show()
# b.showTip()
# ----------------------------------------------------------------------------------------------------------------------
# This part we talk about the iterator
# ----------------------------------------------------------------------------------------------------------------------
# 从技术上讲，在 Python 中，迭代器是实现迭代器协议的对象，它包含方法 __iter__() 和 __next__()。
# ----------------------------------------------------------------------------------------------------------------------
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
#
# print(next(myit))
# print(next(myit))
# print(next(myit))
# text = "apple"
# a = iter(text)
# i = 0
# while i < len(text):
#     print(next(a))
#     i += 1
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)
# ----------------------------------------------------------------------------------------------------------------------
# define a function in a function, total attribute.
# ----------------------------------------------------------------------------------------------------------------------
# def func1():
#     x = 100
#
#     def func2():
#         print(x)
#
#         def func3():
#             print(x + 11)
#
#         func3()
#
#     func2()
#
#
# func1()
# ----------------------------------------------------------------------------------------------------------------------
# This part we need to Quote anther py file(module).
# ----------------------------------------------------------------------------------------------------------------------
# import module
#
# a = module.moduleclass()
# a.modfunc()
# import module as mod
#
# a = mod.moduleclass()
# a.modfunc()
# import module
# import platform  # 内置模块
#
# print(dir(platform))
# from module import person
#
# print(person[2].get('name'))
# ----------------------------------------------------------------------------------------------------------------------
# This part we need to learn use date func(module).
# ----------------------------------------------------------------------------------------------------------------------
# import datetime
#
# x = datetime.datetime.now()
#
# print(x.strftime("%A")) #格式代码 https://www.w3school.com.cn/python/python_datetime.asp
#
# x = datetime.datetime(2020, 5, 17)
#
# print(x)
#
# print(x.strftime("%B"))
#
# ----------------------------------------------------------------------------------------------------------------------
# This part we need to use json.
# ----------------------------------------------------------------------------------------------------------------------
# import json
#
# # 一些 JSON:
# x =  '{ "name":"Bill", "age":63, "city":"Seatle"}'
#
# # 解析 x:
# y = json.loads(x)
#
# # 结果是 Python 字典：
# print(y["age"])
# import json
#
# x = {
#     "name": "Bill",
#     "age": 63,
#     "city": "Seatle"
# }
# y = json.dumps(x)
# print(y)
# ----------------------------------------------------------------------------------------------------------------------
# This part we need to use RegEx.
# ----------------------------------------------------------------------------------------------------------------------
# import re
#
# str = "China is a great country"
# x = re.findall("USA", str)
# print(x)
# import re
#
# str = "China is a great country"
# x = re.search("\s", str)
#
# print("The first white-space character is located in position:", x.start())
# import re
#
# str = "China is a great country"
# x = re.split("\s", str, re.search("\s", str).__sizeof__())
# print(x)
