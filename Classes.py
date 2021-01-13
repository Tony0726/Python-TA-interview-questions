import pandas as pd #导入pandas包读取csv文件

class Finance():
    def __init__(self, filename): #读取文件，返回历史股价字典
        self.read_csv = pd.read_csv(filename ,index_col=0) # 读取整个csv文件，选取日期这一列为索引
        self.price_history = self.read_csv.to_dict(orient='index') # 将dataframe转为字典，index作为关键字
        for key, value in self.price_history.items(): # 遍历字典
            self.price_history[key] = tuple(value.values()) # 将字典的值转为元组

    def average(self): #计算每天的平均股价
        self.price_average = {} #新建一个空字典
        for key, value in self.price_history.items(): #遍历price_history字典
            self.price_average[key] = (value[1] + value[2]) / 2 #计算每天的平均股价，添加到price_average字典
        return self.price_average #返回price_average字典

    def price_search(self, low, high): #返回在low-high之间的日期列表
        dates = self.read_csv.loc[(self.read_csv['Low'] >= low) & (self.read_csv['High'] <= high)] #选取满足条件的行
        dates = list(dates.index) #取满足条件的日期并转为列表
        return dates #返回日期列表

if __name__ == '__main__':
    print("过去一年每日股价信息：")
    apple = Finance('AAPL.csv')  # 创建Finance实例对象
    for key, value in apple.price_history.items():  # 遍历price_history字典
        print(key + ' ' + str(value))  # 输出日期和对应的相关信息
    print("过去一年每日平均股价：")
    apple.average()
    for key, value in apple.price_average.items():  # 遍历price_average字典
        print(key + ' ' + str(value))  # 输出日期和平均股价
    print("过去一年最低股价和最高股价在一定区间内的所有日期：")
    dates = apple.price_search(120, 130)
    print(dates)