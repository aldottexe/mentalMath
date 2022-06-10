import random
import tensorflow as tf
from tensorflow import keras
import numpy as np
import os

part1 = np.random.randint(low=0, high=100, size=100)
part2 = np.random.randint(low=0, high=100, size=100)
sum = part1 + part2
parts = np.column_stack((part1,part2))

model = keras.Sequential([keras.layers.Dense(units=2, input_shape=[2]),
keras.layers.Dense(units=1)])
model.compile(optimizer="adam", loss="mean_squared_error")

model.fit(parts,sum,epochs=200)

quips = ["that's like",
"in the ballpark of",
"probably like"]

print("\n========================= Model Loaded!! ======================\n")
import time

print ("\rready...", end="")
time.sleep(1)
print ("\rsteady...", end="")
time.sleep(1)
print ("\rgo!       ", end="")
time.sleep(.5)


os.system("clear")

while True:
    x = int(input("\nType a number: "))
    y = int(input("Type a number to add to it: "))
    result = model.predict([[x,y]])
    print(f"{x}+{y}")
    print(random.choice(quips),result[0][0])
