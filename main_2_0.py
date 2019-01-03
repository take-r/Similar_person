# coding: UTF-8
import argparse

from chainer.links.caffe import CaffeFunction
from chainercv.transforms import center_crop
import numpy as np
from PIL import Image
import cv2
import datetime


data_folder = './'

def read_img(img_path):
    img = Image.open(img_path).convert('RGB')
    img = img.resize((256,256))
    x = np.array(img, dtype=np.float32)
    # convert RGB image to BGR
    x = x[:, :, ::-1]
    x -= np.array([91.4953, 103.8827, 131.0912], dtype=np.float32)
    x = x.transpose((2, 0, 1))
    x = center_crop(x, (224, 224))
    return x

        

def read_vec(path, num_people):
    pic_names = []
    vecs = []

    with open(path, mode='r') as f:
        l_strip = [s.strip() for s in f.readlines()]
        
        for k in range(num_people):
            pic_names.append(l_strip[2*k])
            vec = l_strip[2*k+1].split()
            vec = [float(s) for s in vec]
            vecs.append(vec)

    return pic_names, vecs

def capture_camera(mirror=True, size=None):
    dt_now = datetime.datetime.now()

    """Capture video from camera"""
    # カメラをキャプチャする
    cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号

    while True:
        # retは画像を取得成功フラグ
        ret, frame = cap.read()

        # 鏡のように映るか否か
        if mirror is True:
            frame = frame[:,::-1]

        # フレームを表示する
        cv2.imshow('camera capture', frame)
        cv2.moveWindow('camera capture', 100, 0)

        k = cv2.waitKey(1) # 1msec待つ
        if k != -1: # 何かしらのキーを押す
            path = "photo_{}_{}_{}_{}.jpg".format(
                (dt_now.day), (dt_now.hour), (dt_now.minute), (dt_now.second))
            cv2.imwrite(path,frame)
            image = frame[:,428-240:428+240].astype(np.float32)
            image -= np.array([91.4953, 103.8827, 131.0912], dtype=np.float32)
        
            #画像をキャプチャ＆保存
            break
        
        # キャプチャを解放する   
        #cap.release()
        #cv2.destroyAllWindows()
    
    return path
            
    #return cv2.resize(image,(224,224))


def main():
    f = CaffeFunction(data_folder + 'resnet50_128.caffemodel')
    
    img_path = capture_camera()
    #frame = frame.resize(256,256)
        
    x = np.stack((read_img(img_path),
                  read_img(img_path)))
    #print(frame.shape)
    #frame = frame.transpose(2,0,1)
    #x = np.stack((frame, frame))
    #x = frame[np.newaxis,]
    y, = f(inputs={'data': x}, outputs=['feat_extract'])
    y = np.squeeze(y.data, axis=(2, 3))
    y_l2norm = np.linalg.norm(y, ord=2, axis=1, keepdims=True)
    normalized_y = y / y_l2norm

    vec_path = data_folder + 'vec_list.txt'
    num_people = 96

        
    pic_names, vecs = read_vec(vec_path, num_people)

    similarity = []
    for k in range(num_people):
        similarity.append(np.dot(normalized_y[0], vecs[k]))
        
    #print(similarity)#全類似度を出力
    print('------------------------------------------------------------------------\n')
    print('\n')

        
    print('あなた と 一番似ている芸能人は　{} で類似度は {} \n'.format(
            pic_names[similarity.index(max(similarity))],
            max(similarity)))
    print('あなた と 一番似てない芸能人は　{} で類似度は {} \n'.format(
            pic_names[similarity.index(min(similarity))],
            min(similarity)))        
    print('\n')
    print('------------------------------------------------------------------------\n')
        
     
     
    print('end')

    # for k in range(num_people):
    #     print('pic1 と {} との類似度: {}'.format(
    #        pic_names[k], (np.dot(normalized_y[0], vecs[k]))))

    


if __name__ == '__main__':
    main()
    #capture_camera()