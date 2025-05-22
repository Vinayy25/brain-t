import os
import cv2
import numpy as np
from tensorflow import keras
from sklearn.model_selection import train_test_split
from keras.utils import normalize, to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense

# Directory and file handling
image_directory = './'  # Use relative path to current directory
no_tumor_images = os.listdir(os.path.join(image_directory, 'no'))
yes_tumor_images = os.listdir(os.path.join(image_directory, 'yes'))

print(f"Found {len(no_tumor_images)} 'no tumor' images and {len(yes_tumor_images)} 'tumor' images")

dataset = []
label = []
INPUT_SIZE = 64

# Load images from 'no' folder
for i, image_name in enumerate(no_tumor_images):
    if image_name.endswith('.jpg'):
        image_path = os.path.join(image_directory, 'no', image_name)
        image = cv2.imread(image_path)
        if image is None:
            print(f"Warning: Could not load image {image_path}")
            continue
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (INPUT_SIZE, INPUT_SIZE))
        dataset.append(image)
        label.append(0)

# Load images from 'yes' folder
for i, image_name in enumerate(yes_tumor_images):
    if image_name.endswith('.jpg'):
        image_path = os.path.join(image_directory, 'yes', image_name)
        image = cv2.imread(image_path)
        if image is None:
            print(f"Warning: Could not load image {image_path}")
            continue
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (INPUT_SIZE, INPUT_SIZE))
        dataset.append(image)
        label.append(1)

print(f"Processed {len(dataset)} images in total")

dataset = np.array(dataset)
label = np.array(label)

# Split the data
x_train, x_test, y_train, y_test = train_test_split(dataset, label, test_size=0.2, random_state=0)

# Normalize the data
x_train = x_train / 255.0
x_test = x_test / 255.0

# One-hot encode the labels
y_train = to_categorical(y_train, num_classes=2)
y_test = to_categorical(y_test, num_classes=2)

# Model building
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(INPUT_SIZE, INPUT_SIZE, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3), kernel_initializer='he_uniform'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), kernel_initializer='he_uniform'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(2))
model.add(Activation('softmax'))

# Model summary
model.summary()

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
print("Training model...")
history = model.fit(x_train, y_train, batch_size=16, verbose=1, epochs=10, validation_data=(x_test, y_test), shuffle=False)

# Save the model
model.save('BrainTumor.h5')
print("Model saved as 'BrainTumor.h5'")

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f'Test accuracy: {accuracy * 100:.2f}%')
