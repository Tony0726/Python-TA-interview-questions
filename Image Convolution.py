import cv2
import numpy as np

def blur(videopath, kernel, savepath):
    vid = cv2.VideoCapture(videopath)
    video_width = int(vid.get(3)) #获取视频的宽
    video_height = int(vid.get(4)) #获取视频的高
    video_fps = int(vid.get(5)) #获取视频的帧速率
    #创建VideoWriter类对象
    fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0') #创建视频编解码器
    out = cv2.VideoWriter(savepath, fourcc, video_fps, (video_width, video_height)) #关键视频流写入对象

    while(vid.isOpened()): #当时视频可以打开时
        ret, frame = vid.read()	#捕获一帧图像
        if ret==True: #存在这一帧
            frame = cv2.filter2D(frame, -1, kernel) #利用内核实现对图像的卷积运算
            out.write(frame) #写入帧

            img_ori = cv2.resize(frame, (640, 360)) #调整大小为了屏幕显示得下
            cv2.imshow('frame',img_ori)  #显示帧
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    vid.release() #释放读取
    out.release() #释放写入
    cv2.destroyAllWindows() #关闭所有窗口

if __name__ == '__main__':
    filename = 'highway_video.mp4'  # 视频路径
    kernel = np.array((
        [2, 4, 5, 4, 2],
        [4, 9, 12, 9, 4],
        [5, 12, 15, 12, 5],
        [4, 9, 12, 9, 4],
        [2, 4, 5, 4, 2]), dtype="float32") / 159  # 卷积核
    blur(filename, kernel, savepath='output.avi')  # 模糊视频并保存