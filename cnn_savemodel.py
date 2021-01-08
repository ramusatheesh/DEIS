import cv2
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


#path = r'E:\Project DEIS\CNN\img.jpg'
#img=cv2.imread(path)
#while(1):
 #      cv2.imshow("image",img)

#       if cv2.waitKey(25) & 0xFF == ord('q'):
 #        break
#cv2.destroyAllWindows()

train_path=r"E:\project\CNN\Training"
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
  train_path,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(180, 180),
  batch_size=32)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  train_path,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(180,180),
  batch_size=32)

class_names = train_ds.class_names


Height = 180
Width = 180
Classes = 2
model = Sequential([
  layers.experimental.preprocessing.Rescaling((1.0/255), input_shape=(Height, Width, 3)),
  layers.Conv2D(8, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='valid', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='valid', activation='sigmoid'),
  layers.MaxPooling2D(),
  layers.Conv2D(128, 3, padding='same', activation='sigmoid'),
  layers.MaxPooling2D(),
  layers.Conv2D(256, 3, padding='same', activation='tanh'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(1024, activation='relu'),
  layers.Dense(Classes)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
epochs=100
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)


save=r"E:\Project DEIS\CNN"
model.save(save)
#with open('Pickle_Model', 'wb') as file:  
   # pickle.dump(history, file)



path= r'E:\project\CNN\img.jpg'

img = keras.preprocessing.image.load_img(
    path, target_size=(Height, Width)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch
predictions=model.predict(img_array)
score = tf.nn.softmax(predictions[0])
print(
    "I am {:.2f} sure that This is a {} Shape"
    .format( 100 * np.max(score),class_names[np.argmax(score)])
)

