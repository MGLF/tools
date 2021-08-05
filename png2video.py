# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:09:07 2019

@author: Chen Yongfu
"""
import os
import cv2
import time
# 图片合成视频
def picvideo(path, size=(1920,1080), extension = '.png', fps=20, fcc='MJPG', isFlip = False, flipType=-1):
    '''
    本函数为读取图片生成视频的
    需要保证图片为同格式，同尺寸，相同格式意味着要编码一致
    path, 图像路径
    size, 视频生成尺寸
    fps， 幀速
    fcc, 编码格式
        视频编码参考：
        I420，无损压缩
        MJPG DIVX XVID
        CV_FOURCC('P','I','M','1') = MPEG-1 codec
        CV_FOURCC('M','J','P','G') = motion-jpeg codec
        CV_FOURCC('M', 'P', '4', '2') = MPEG-4.2 codec
        CV_FOURCC('D', 'I', 'V', '3') = MPEG-4.3 codec
        CV_FOURCC('D', 'I', 'V', 'X') = MPEG-4 codec
        CV_FOURCC('U', '2', '6', '3') = H263 codec
        CV_FOURCC('I', '2', '6', '3') = H263I codec
        CV_FOURCC('F', 'L', 'V', '1') = FLV1 codec
        https://www.cnblogs.com/Akagi201/archive/2012/04/03/2430772.html
    isFlip
    flipCode，翻转模式：0 垂直翻转；1 水平翻转； -1 水平垂直翻转
    '''
    filelist = os.listdir(path) #获取该目录下的所有文件名
    # 导出路径
    file_path = './result.avi'
    # 不同视频编码对应不同视频格式和大小，压缩率
    fourcc = cv2.VideoWriter_fourcc(*fcc)
    video = cv2.VideoWriter(file_path, fourcc, fps, size )

    for i in range(325,10584):
        p = '%05d' % i
        st = '/home/lab/GLF_Data/superpoint/SuperPointPretrainedNetwork/myoutput/'+'frame_'+str(p)+'.png' #图片存放路径
        if os.path.exists('/home/lab/GLF_Data/superpoint/SuperPointPretrainedNetwork/myoutput/'+'frame_'+str(p)+'.png'):    #判断图片是否存在
            img = cv2.imread(filename=st)
            img = cv2.resize(img, size)
            if isFlip:
                img = cv2.flip(img, flipType)
            cv2.imshow('video', img)
            cv2.waitKey(1)
            video.write(img)    # 把图片写进视频

    video.release() # 释放
    cv2.waitKey(1)&0xFF
    cv2.destroyAllWindows()

if __name__ == '__main__':
        picvideo(r'/home/lab/GLF_Data/SuperPointPretrainedNetwork/myoutput', (1280, 720))
