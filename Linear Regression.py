import csv #导入csv包为了读取数据
import datetime #导入datetime包为了计算日期间的差
import numpy as np #导入numpy包为了将数据转换为numpy.ndarray格式用于线性回归
from sklearn.linear_model import LinearRegression #导入线性回归函数

#读取数据并返回字典
def read(path):
    dic = {}
    with open(path, 'r') as f:
        reader = csv.reader(f)
        n = 1
        for line in reader:
            if n == 1:
                for i in range(len(line)):
                    if line[i] == 'Date': #确定日期是第几列返回索引
                        date = i
                        continue
                    if line[i] == 'Close': #确定收盘价是第几列返回索引
                        close = i
                        break
                n = n + 1
            else:
                dic[line[date]] = float(line[close])
        return dic

if __name__ == '__main__':
    dic = read('AAPL.csv')  # 读取文件
    n = 0  # 区分第一次和后面
    start = ''  # 用于存放第一天日期也就是the last 364-th day
    x = []  # 存放第几天的列表
    for key, value in dic.items():
        if n == 0:
            start = datetime.datetime.strptime(key, '%Y-%m-%d')  # 将日期从str转为timedelta格式
            x.append(n)
            n = n + 1
        else:
            cur = datetime.datetime.strptime(key, '%Y-%m-%d')  # 将日期从str转为timedelta格式
            dif = cur - start  # 计算日期差值
            x.append(dif.days)  # 将差值添加至x列表
    x = np.array(x).reshape((-1, 1))  # 将第几天列表转换为numpy.ndarray格式
    y = np.array(list(dic.values()))  # 将收盘价也转换为numpy.ndarray格式
    model = LinearRegression()  # 创建线性回归模型
    model = model.fit(x, y)  # 训练模型
    print('模型的系数a为:', model.coef_)
    print('模型的截距b为:', model.intercept_)
    print('模型的衡量指标R Squared：',
          model.score(x, y))  # 预测数据与原始数据均值之差的平方和/原始数据和原始数据均值之差的平方和
    print("今天的股价是：", model.predict([[365]]))  # 预测今天的收盘价
    print("30天后的股价是：", model.predict([[365 + 30]]))  # 预测30天后的收盘价