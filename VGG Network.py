import keras
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras import regularizers
from keras.models import load_model
from keras.models import Sequential

# class VGG_16:
#     def __init__(self):
#         self.num_classes = 10
#         self.weight_decay = 0.0005
#         self.x_shape = [32, 32, 3]
#         self.model = self.build_model()
#         self.model.load_weights('cifar10vgg.h5')
#
#     def build_model(self):
#         model = Sequential()
#         weight_decay = self.weight_decay
#
#         model.add(Conv2D(64, (3, 3), padding='same',
#                          input_shape=self.x_shape,kernel_regularizer=regularizers.l2(weight_decay)))#卷积
#         model.add(Activation('relu'))#激活层去线性
#         model.add(BatchNormalization())#标准化加快收敛
#         model.add(Dropout(0.3))#防止过拟合
#
#         model.add(Conv2D(64, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#
#         model.add(MaxPooling2D(pool_size=(2, 2)))#池化层
#
#         model.add(Conv2D(128, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#         model.add(Dropout(0.4))
#
#         model.add(Conv2D(128, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#
#         model.add(MaxPooling2D(pool_size=(2, 2)))
#
#         model.add(Conv2D(256, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#         model.add(Dropout(0.4))
#
#         model.add(Conv2D(256, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#         model.add(Dropout(0.4))
#
#         model.add(Conv2D(256, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#
#         model.add(MaxPooling2D(pool_size=(2, 2)))
#
#
#         model.add(Conv2D(512, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#         model.add(Dropout(0.4))
#
#         model.add(Conv2D(512, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#         model.add(Dropout(0.4))
#
#         model.add(Conv2D(512, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#
#         model.add(MaxPooling2D(pool_size=(2, 2)))
#
#
#         model.add(Conv2D(512, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#         model.add(Dropout(0.4))
#
#         model.add(Conv2D(512, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#         model.add(Dropout(0.4))
#
#         model.add(Conv2D(512, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#
#         model.add(MaxPooling2D(pool_size=(2, 2)))
#         model.add(Dropout(0.5))
#
#         model.add(Flatten())
#         model.add(Dense(512,kernel_regularizer=regularizers.l2(weight_decay)))#全连接层
#         model.add(Activation('relu'))
#         model.add(BatchNormalization())
#
#         model.add(Dropout(0.5))
#         model.add(Dense(self.num_classes))#全连接层
#         model.add(Activation('softmax'))#softmax层
#         return model

from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.applications.vgg16 import VGG16
import numpy as np

if __name__ == '__main__':
    #加载模型
    model = VGG16(include_top=True, weights='imagenet', input_tensor=None,
                  input_shape=None, pooling=None, classes=1000)
    img = image.load_img('1.jpeg', target_size=(224, 224)) # 读取图片
    x = image.img_to_array(img)  # 将图片转换为矩阵 三维（224，224，3）
    x = np.expand_dims(x, axis=0)  # 四维（1，224，224，3）
    x = preprocess_input(x)  # 预处理
    y_pred = model.predict(x)  # 预测概率
    print("测试图：", decode_predictions(y_pred))  # 输出五个最高概率(类名, 语义概念, 预测概率)