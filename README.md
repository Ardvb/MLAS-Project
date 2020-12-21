# Machine learning and statistics Project

### Author: Arnoud van Balkom
- Lecturer: Dr. Ian Mcloughlin
- Email: G00376518@gmit.ie

## Getting started
- Download [Anaconda](https://www.anaconda.com/)

- Follow these steps to download and run this repository:

1. Go to my repository on Github: https://github.com/Ardvb/MLAS-Project
2. Click the clone or download button.
3. Save the repository to your device.
4. Install [Docker](https://www.docker.com/products/docker-desktop) to create image
5. Go to the folder where the files are downloaded and type: "docker build -t MLAS-Project".
6. After the Docker image has been created, type "docker run == name MLAS-container -d -p 5000:5000 MLAS-project".
7. The HTML page can now be accessed at: http://127.0.0.1:5000/

## Contents of this repository

- Jupyter Notebook in which 3 models are trained and tested using the <i>powerproduction</i> dataset.
- Python script called server.py that runs a web service in a container
- Python scripts for gradient booster model, and random forest model
- Dockerfile that runs the web service in a container
- HTML page linked to server.py which will allow user to enter wind speed value and get corresponding power output returned.

## Sources used when creating this repository

1. https://realpython.com/train-test-split-python-data/ # Splitting dataset in train and test parts
2. https://towardsdatascience.com/understanding-gradient-boosting-machines-9be756fe76ab # Gradient Boosting
3. https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/ # Gradient Boosting
4. https://medium.com/datadriveninvestor/random-forest-regression-9871bc9a25eb # Random Forest explained
5. https://stackoverflow.com/questions/61246741/how-to-take-user-input-from-a-single-line-in-numpy-array # Taking user input in Numpy Array
6. https://www.geeksforgeeks.org/drop-rows-from-the-dataframe-based-on-certain-condition-applied-on-a-column/ # How to select certain rows from a Pandas Dataframe
7. https://web.microsoftstream.com/video/4486d827-1d6b-481a-a570-a6264ddf1c43 Video on regression using skikit-learn by Ian Mcloughlin
