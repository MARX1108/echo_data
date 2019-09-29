from __future__ import absolute_import, division, print_function
import sys
import tensorflow as tf
import os
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from PIL import Image
from tensorflow.keras import datasets, layers, models


IMG_SIZE_X = 437
IMG_SIZE_Y = 308

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)




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
            temp_array = crop_img(folderPath+"/"+pic, 329, 25, 791, 584)

        
            if (check_array(temp_array)):
              temp_array = cv2.resize(temp_array, (IMG_SIZE_Y, IMG_SIZE_X))
              img_array = np.array(temp_array)
              img_array = img_array / 255
              images_array[i] = img_array
              #cv2.imshow("win", images_array[i])
              labels_array[i] = label
              i += 1
              
        label += 1
        
    return images_array[200:1800], labels_array[200:1800], images_array[0:2056:3], labels_array[0:2056:3]

def crop_img(filename, left, top, right, bottom):
    im = Image.open(filename) 
    return im.crop((left, top, right, bottom)) 
    #im1.show() 
    #crop_img(folderPath+"/"+pic, 329, 25, 791, 584)
    # 300, 25, 700,650
    #width of 27.6 px/ms
    #crop_img(os.getcwd()+"/Fig/mic0/echo4/0-static-148-20190904_072254225977.jpg", 329, 25, 791, 584)

def load_image( infilename ) :
    img = Image.open( infilename )
    img.crop((329, 25, 791, 584))
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

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

'''
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(IMG_SIZE_X, IMG_SIZE_Y, 3)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(512, activation=tf.nn.softmax),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dropout(0.1),
  tf.keras.layers.Dense(512, activation='softmax')
])

print("Model compling")
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5,  batch_size=12)
model.evaluate(x_test, y_test, batch_size=12)
'''


model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE_X, IMG_SIZE_Y, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5,  batch_size=12)
model.evaluate(x_test, y_test, batch_size=12)


print("program finished")