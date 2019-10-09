import tensorflow as tf
from tensorflow.keras import models
import numpy as np
import matplotlib.pyplot as plt


mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

""" model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']) """

#model.fit(x_train, y_train, epochs=5)
#model.evaluate(x_test, y_test)

#model.save("minst.h5")
model = models.load_model("minst.h5")
predict = model.predict(x_test)




f = np.array(predict)
print(predict[1][2])
print(f[1,2])
plt.imshow(f, interpolation="nearest", origin="upper")
plt.colorbar()
plt.show()
print(predict[0])