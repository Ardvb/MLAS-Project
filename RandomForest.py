# pylint: disable=no-member  
# Above statement is just to disable an error message

# To read in dataset
import pandas as pd   

# for numerical work
import numpy as np

# to use randomforest regression model
from sklearn.ensemble import RandomForestRegressor

# To turn array into list, html page can handle it
import json 


windpower = pd.read_csv('https://raw.githubusercontent.com/ianmcloughlin/2020A-machstat-project/master/dataset/powerproduction.csv')

windpowernew = windpower.drop(windpower[(windpower["speed"]> 10) & (windpower["power"]==0)].index) # Don't use speed values above 10 with a corresponding power output of 0

class RanFModel:
    def rfmodel(windspeed): 
      x = windpowernew.speed.values.reshape(-1,1) # Reshape to values between -1 and 1 so we can use regression analysis
      y = windpowernew["power"]
      modelrf = RandomForestRegressor()
      modelrf.fit(x,y) 
      windspeed = np.array((windspeed).split(), dtype='float') # Split the input string into a list. Then convert the list into a numpy array.
      # Adapted from https://stackoverflow.com/questions/61246741/how-to-take-user-input-from-a-single-line-in-numpy-array

      windspeedrs = windspeed.reshape(-1,1) # Reshape the array to fit the model
      power_output = modelrf.predict(np.array(windspeedrs)) # Predict power output using wind speed (output is an array)
      powerlist = power_output.tolist() # Turn array into list so it can be read into html file # Adapted from https://www.kite.com/python/answers/how-to-serialize-a-numpy-array-into-json-in-python
      powerjson = json.dumps(*powerlist) # Add * to get rid of the brackets
      return{"value": powerjson} # Return value to be outputted on html page

