import flask as fl
import numpy as np
#from GradBoosting import GradBoosting as gb     
#from RandomForest import RandomForest as rf  


# Create Web App
app = fl.Flask(__name__, static_url_path = '', static_folder = 'staticpages')


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform(low=1.0, high=24.0)}

@app.route('/api/grad')
def grad():
  return {"value": np.random.uniform(low=1.0, high=24.0)}

@app.route('/api/randfor')
def randfor():
  return {"value": np.random.uniform(low=1.0, high=24.0)}

#@app.route('/gradboost/<string:windpowernew>')
#def gradboostpred(windpowernew):
    
    # String must be converted to float as cannot pass natively
    # Insight from https://github.com/pallets/flask/issues/315
    #windpowernew = float(windpowernew)
    #return gb.gbrmodel(windpowernew)




if __name__ == "__main__":
    app.run(debug = True)