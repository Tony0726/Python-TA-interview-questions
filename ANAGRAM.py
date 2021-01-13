import operator

origin = 'Tom Marvel Riddle'
test = 'I am Lord Voldemort'

origin = list(origin.replace(' ', '').lower())  # 将所有空格去除并将字母变为小写再转为列表
test = list(test.replace(' ', '').lower())  # 将所有空格去除并将字母变为小写再转为列表

origin.sort()  # 给列表排序
test.sort()  # 给列表排序

is_anagram1 = operator.eq(origin, test) #判断列表是否相同
print("字母个数必须相同时的结果:" + str(is_anagram1))

is_anagram2 = operator.eq(set(origin), set(test)) #判断集合是否相同
print("字母个数可以不同时的结果:" + str(is_anagram2))