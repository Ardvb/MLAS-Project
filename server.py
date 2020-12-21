# Import Flask for web app
import flask as fl

# To be able to use Gradient Boosting Model
from GradBoosting import GradModel

# To be able to use Random Forest Model
from RandomForest import RanFModel

# To generate random number
import numpy as np
 
# Create Web App
app = fl.Flask(__name__, static_url_path = '', static_folder = 'staticpages')


# Route for home page
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Route for predicting power-output using Gradient Boosting model
@app.route('/api/gradient/<string:inpspeed>') 
def grboosting(inpspeed):
  return GradModel.gbmodel(inpspeed)

# Route for predicting power-output using Random Forest Model
@app.route('/api/randfor/<string:inpspeed>') 
def randforest(inpspeed):
  return RanFModel.rfmodel(inpspeed)

# Route to generate random number between 1 and 24
@app.route('/api/random') 
def random():
  return {"value": round(np.random.uniform(low=1.0, high=24.0),2)}

if __name__ == "__main__":
    app.run(debug = True)