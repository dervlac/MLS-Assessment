# for neural networks.
import tensorflow.keras as kr
# for numerical arrays
import numpy as np
# for data frames.
import pandas as pd
# for plotting
import matplotlib.pyplot as plt
# for test and train datasets
import sklearn.model_selection as mod
# flask for web app.
import flask as fl

# lines 15 to 26 pulled from jupyter notebook analysis
df = pd.read_csv("https://raw.githubusercontent.com/ianmcloughlin/2020A-machstat-project/master/dataset/powerproduction.csv")

data = df.drop([208,340,404,456,490,491,492,493,494,495,496,497,498,499], axis=0)
data.reset_index(inplace=True)

model = kr.models.Sequential()
model.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="random_normal", bias_initializer="zeros"))
model.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="random_normal", bias_initializer="zeros"))
model.add(kr.layers.Dense(1, activation='linear', kernel_initializer="ones", bias_initializer="zeros"))
model.compile('adam', loss='mean_squared_error')

model.fit(data['speed'], data['power'], epochs=200, batch_size=10)

# Create a new web app.
app = fl.Flask(__name__)

@app.route("/<int:speed>")
def predict(speed):
    return model.predict(speed)

if __name__ == "__main__":
    app.run(debug = True)