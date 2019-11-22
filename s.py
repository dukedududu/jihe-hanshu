'''
basket ={'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)#自动去重复的元素
print('apple' in basket)#快速判断 元素是否在集合中
'''
a=set('abcahgachiug')
b=set('oasofchowhljm')
'''
print(a-b)# 集合a中包含而集合b中不包含的元素
print(a&b)# 集合a和b中都包含了的元素
print(a|b)# 集合a或b中包含了的元素
print(a^b)# 不同时包含于a和b的元素
'''

#能够添加元素的函数
a.add('fan')
print(a)

b.update([1,2,3])#参数可以是列表，元组，字典等
print(b)

#能够移除元素的函数
a.remove('fan')#如果a没有 会报错
print(a)

b.discard('fan')#如果b没有 不会报错
print(b)

a.pop()#随机删除集合中的一个元素
print(a)