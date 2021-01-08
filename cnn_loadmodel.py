import tensorflow as tf
from tensorflow import keras
import numpy as np


save=r"E:\Project DEIS\CNN"

loaded_model = tf.keras.models.load_model(save)


path= r'E:\project\CNN\img.jpg'

Height = 180
Width = 180

class_names=['BLOCKED', 'FREE']
img = keras.preprocessing.image.load_img(
    path, target_size=(Height, Width)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch
predictions=loaded_model.predict(img_array)
score = tf.nn.softmax(predictions[0])
print(
    "The Way is"
    ,class_names[np.argmax(score)])
