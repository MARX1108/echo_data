from __future__ import absolute_import, division, print_function, unicode_literals
import sys
import tensorflow as tf
import os
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from PIL import Image

IMG_SIZE_X = 656
IMG_SIZE_Y = 875




def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

def load_data(micName, IMG_SIZE_X, IMG_SIZE_Y):
    this_path = os.getcwd()
    #print(this_path)
    filePath =  this_path + "/Fig/" + micName
    folderList = os.listdir(filePath)
    #print(fileList)
    dataset_size = 0
    for folder in folderList:
        folderPath = filePath + "/" + folder
        picList = os.listdir(folderPath)
        picList = [k for k in picList if '.jpg' in k]
        dataset_size = dataset_size + len(picList)
        

    images_array = np.empty((dataset_size,IMG_SIZE_X,IMG_SIZE_Y,3), dtype=float, order='C')
    labels_array = np.empty((dataset_size,1), dtype=float, order='C')
    

    i = 0
    label = 4
    for folder in folderList:
        folderPath = filePath + "/" + folder

        picList = os.listdir(folderPath)
        picList = [k for k in picList if '.jpg' in k]
        #print(picList)
        for pic in picList:
            
            """ if os.path.exists(folderPath+"/"+pic):
                print("pass")
            else:
                print(folderPath+"/"+pic) """

            #temp_array = cv2.imread(folderPath+"/"+pic)
            temp_array = load_image(folderPath+"/"+pic)

        
            if (check_array(temp_array)):
              #temp_array = cv2.resize(temp_array, (IMG_SIZE_Y, IMG_SIZE_X))
              img_array = np.array(temp_array)
              img_array = img_array / 255
              images_array[i] = img_array
              #cv2.imshow("win", images_array[i])
              labels_array[i] = label
              i += 1
              
        label += 1
        
    return images_array[1:2056], labels_array[1:2056], images_array[0:2056:2], labels_array[0:2056:2]

def crop_img(filename, left, top, right, bottom):
    im = Image.open(filename) 
    return im.crop((left, top, right, bottom)) 
    #im1.show() 
    #crop_img(folderPath+"/"+pic, 329, 25, 791, 584)
    # 300, 25, 700,650
    #width of 27.6 px/ms
    #crop_img(os.getcwd()+"/Fig/mic0/echo4/0-static-148-20190904_072254225977.jpg", 329, 25, 791, 584)



def check_array(x):
    try:
        x.shape
        return True
    except:
        return False




str = os.getcwd() + "\Fig\mic0\echo5/0-static-977-2019y9m8d21h45m17s37.280242lat-80.474363long.jpg"
open(str)
print(str)
image = load_image(str)


x_train, y_train, x_test, y_test = load_data("mic0", IMG_SIZE_X, IMG_SIZE_Y)


model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(IMG_SIZE_X, IMG_SIZE_Y, 3)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1,  batch_size=128)
model.evaluate(x_test, y_test, batch_size=128)


print("program finished")
