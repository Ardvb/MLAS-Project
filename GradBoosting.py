import pandas as pd   
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

# To split dataset into train and test parts
from sklearn.model_selection import train_test_split

windpower = pd.read_csv('https://raw.githubusercontent.com/ianmcloughlin/2020A-machstat-project/master/dataset/powerproduction.csv')

windpowernew = windpower.drop(windpower[(windpower["speed"]> 10) & (windpower["power"]==0)].index)

class GradBoosting:
    def gbrmodel(self, x):
      
      x = windpowernew.speed.values.reshape(-1,1) # Reshape to values between -1 and 1 so we can use regression analysis later
      y = windpowernew["power"]

      x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0) # Using random state to make test reproducible.

      modelgbr = GradientBoostingRegressor(random_state=0).fit(x_train, y_train)
      modelgbr.score(x_test, y_test)

  # Make Prediction Using Wind Speed
      prediction = modelgbr.predict([x])

        # Stores elemtent of array as variable so can be returned
      result = round(np.ndarray.item(prediction[0]),2)

      return {"value": result}