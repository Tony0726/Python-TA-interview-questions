from collections import deque

def dequeue(queue): #递归函数实现queue.popleft的功能
    flag = True #标签用来标记是否是最后一个数
    if len(queue): #queue长度大于0时pop
        a = queue.pop()
        if len(queue) == 0: #如果pop后为空则给flag赋值False，也就是不用append最后一个数
            flag = False
    else:
        return queue #长度为空时返回queue
    ans = dequeue(queue) #递归调用
    if flag:
        ans.append(a) #当不是最后一个数时添加
    return ans #返回queue

list = range(1,10)
mydeque = deque()
mydeque.extend(list)
print("出队前：" + str(mydeque))
mydeque = dequeue(mydeque)
print("出队后：" + str(mydeque))