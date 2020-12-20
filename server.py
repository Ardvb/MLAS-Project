# Import Flask for web app
import flask as fl

# To be able to use Gradient Boosting Model
from GradBoosting import GradModel

# To be able to use Random Forest Model
from RandomForest import RanFModel
import numpy as np
 
# Create Web App
app = fl.Flask(__name__, static_url_path = '', static_folder = 'staticpages')



@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/gradient/<string:inpspeed>') 
def grboosting(inpspeed):
  return GradModel.gbmodel(inpspeed)

@app.route('/api/randfor/<string:inpspeed>') 
def randforest(inpspeed):
  return RanFModel.rfmodel(inpspeed)

@app.route('/api/random') 
def random():
  return {"value": round(np.random.uniform(low=1.0, high=24.0),2)}

if __name__ == "__main__":
    app.run(debug = True)