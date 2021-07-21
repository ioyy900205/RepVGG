'''
Date: 2021-07-17 11:50:52
LastEditors: Liuliang
LastEditTime: 2021-07-17 14:30:11
Description: 
'''
from collections import Iterable,Iterator,Generator

# #1实现了__iter__方法就是iterable

# # class IterObj:
    
# #     def __iter__(self):
# #         # 这里简单地返回自身
# #         # 但实际情况可能不会这么写
# #         # 而是通过内置的可迭代对象来实现
# #         # 下文的列子中将会展示
# #         return self 

# class IterObj:

#     def __init__(self):
#         self.a = [3, 5, 7, 11, 13, 17, 19]

#     def __iter__(self):
#         return iter(self.a)



# it = IterObj()
# print(isinstance(it, Iterable))  # true
# print(isinstance(it, Iterator))  # false
# print(isinstance(it, Generator)) # false




# #2 常见的可迭代对象

# # 在Python中有哪些常见的可迭代对象呢？

# # 1集合或序列类型（如list、tuple、set、dict、str）
# # 2文件对象
# # 3在类中定义了__iter__()方法的对象，可以被认为是 Iterable对象，但自定义的可迭代对象要能在for循环中正确使用，就需要保证__iter__()实现必须是正确的（即可以通过内置iter()函数转成Iterator对象。关于Iterator下文还会说明，这里留下一个坑，只是记住iter()函数是能够将一个可迭代对象转成迭代器对象，然后在for中使用）
# # 4在类中实现了如果只实现__getitem__()的对象可以通过iter()函数转化成迭代器但其本身不是可迭代对象。所以当一个对象能够在for循环中运行，但不一定是Iterable对象。

# print(isinstance([], Iterable))  # true list 是可迭代的
# print(isinstance({}, Iterable))  # true 字典是可迭代的
# print(isinstance((), Iterable))  # true 元组是可迭代的
# print(isinstance(set(), Iterable))  # true set是可迭代的
# print(isinstance('', Iterable))  # true 字符串是可迭代的
# import os
# currPath = os.path.dirname(os.path.abspath(__file__))
# with open(currPath+'/test.py') as file:
#     print(isinstance(file, Iterable)) # true


# for i in it:
#     print(i)
    

# class IterObj:
    
# #     def __init__(self):
# #         self.a = [3, 5, 7, 11, 13, 17, 19]
    
# #     def __getitem__(self, i):
# #         return self.a[i]


# # it = IterObj()
# # print(isinstance(it, Iterable)) # false
# # print(isinstance(it, Iterator)) # false
# # print(isinstance(it, Generator)) #false
# # print(hasattr(it, "__iter__")) # false
# # print(iter(it)) # <iterator object at 0x10b231278>

# # # print(isinstance(iter(it), Iterator))

# # for i in it:
# #     print(i) # 将打印出3、5、7、11、13、17、19

# class IterObj:

#     def __init__(self):
#         self.a = [3, 5, 7, 11, 13, 17, 19]

#         self.n = len(self.a)
#         self.i = 0

#     def __iter__(self):
#         return iter(self.a)

#     def __next__(self):
#         while self.i < self.n:
#             v = self.a[self.i]
#             self.i += 1
#             return v
#         else:
#             self.i = 0
#             raise StopIteration()

# it = IterObj()
# print(isinstance(it, Iterable)) # true
# print(isinstance(it, Iterator)) # true
# print(isinstance(it, Generator)) # false
# print(hasattr(it, "__iter__")) # true
# print(hasattr(it, "__next__")) # true

# print(isinstance([], Iterator)) # false
# print(isinstance({}, Iterator)) # false
# print(isinstance((), Iterator)) # false
# print(isinstance(set(), Iterator)) # false
# print(isinstance('', Iterator)) # false

# print(next(it))
# print(next(it))


# # 3 Generator
# #.1 列表生成器
# g = (x*2 for x in range(10))
# print(g)
# print(isinstance(g, Iterable)) # true
# print(isinstance(g, Iterator)) # true
# print(isinstance(g, Generator)) # true
# print(hasattr(g, "__iter__")) # true
# print(hasattr(g, "__next__")) # true
# print(next(g)) # 0
# print(next(g)) # 2
# print(next(g)) 
# #.2使用yield定义生成器函数



# def gen():
#     for i in range(10):
#         yield i 


def producer(c):
    n = 0
    while n < 5:
        n += 1
        print('producer {}'.format(n))
        r = c.send(n)
        print('consumer return {}'.format(r))


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('consumer {} '.format(n))
        r = 'ok'


if __name__ == '__main__':
    c = consumer()
    next(c)  # 启动consumer
    producer(c)