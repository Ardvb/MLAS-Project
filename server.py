import flask as fl
from GradBoosting import GradBoosting as gb     
from RandomForest import RandomForest as rf  


# Create Web App
app = fl.Flask(__name__, static_url_path = '', static_folder = 'staticpages')

@app.route('/')
def home():
    return app.send_static_file('index.html')

# Route Wind Speed Request to Sigmoid Neural Network Model
@app.route('/api/gradboosting/<string:windpowernew>')
def gradboostpred(windpowernew):
    
    # String must be converted to float as cannot pass natively
    # Insight from https://github.com/pallets/flask/issues/315
    windpowernew = float(windpowernew)
    return gb.gbrmodel(windpowernew)

if __name__ == "__main__":
    app.run(debug = True)