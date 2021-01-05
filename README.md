# Machine Learning and Statistics

## 2020 Assessment

***

This repository documents the project submission for the 2020 Machine Learning and Statistics module in GMIT.

For any queries not covered herein, please contact G00283361@gmit.ie

***

## File Overview

 - **model.py:** this file was used to compile the neural network used to predict the power produced for a given windspeed;
 
 - **turbine_model:** this file is the output of running the model.py file, and is the power predictor which has been trained using the dataset provided for the assessment;
 
 - **MLS Project.ipynb:** the jupyter notebook used to investigate the best approach to use for the neural network predictor;
 
 - **requirements.txt:** the minimum package requirements to run the webservice;
 
 - **dockerfile:** allows the webservice to be run in a docker container;
 
 - **static:** folder containing static pages for the web service.
 
***

## Running the Web Service

In order to produce your own instance of this web service, begin by cloning this repository to your local machine.

This repository contains the required files to allow you to run this web service on a local server, within a virtual environment, or within a docker container.

Get the web service running on Windows by executing:

> python server.py

OR:

> set FLASK_APP = server.py

> python -m flask run

***
