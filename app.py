from pycaret.classification import *
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
from flask import Flask, render_template, request, url_for
from flask import jsonify
import os
import json

# fromflask
# create flask App
app = Flask(__name__)

# write 
# dataset = pd.read_csv(r"D:\University_Projects\Vibration_Analyzer\all_data.csv", header = None)
# dataset.columns = ['tachometer_signals', 'uba_axial_direction', 'uba_radiale_direction', 'uba_tangential_direction', 'oba_axial_direction', 'oba_radiale_direction', 'oba_tangential_direction', 'microphone', 'faults']
# data = dataset.sample(frac=1, random_state=786, ignore_index = True) 

# s = setup(data = data, target = 'faults', session_id = 123)
# best = compare_models()
# save_model(best,'best_model')
# model = load_model('best_model')

#predict
# def predict(model, input_df):
#     predictions_df = predict_model(estimator = model, data = input_df)
#     return predictions_df
    # predictions = predictions_df['Label'][0]
    # return predictions

# Define its route
@app.route("/loaded_model1", methods=["GET"])
def loaded_model1():
    tachometer_signals = request.args.get('tachometer_signals')
    uba_axial_direction = request.args.get('uba_axial_direction')
    uba_radiale_direction = request.args.get('uba_radiale_direction')
    uba_tangential_direction = request.args.get('uba_tangential_direction')
    oba_axial_direction = request.args.get('oba_axial_direction')
    oba_radiale_direction = request.args.get('oba_radiale_direction')
    oba_tangential_direction = request.args.get('oba_tangential_direction')
    microphone = request.args.get('microphone')
    # print(tachometer_signals)
    # tachometer_signals = float(tachometer_signals)
    input_dict = {'tachometer_signals' : float(tachometer_signals), 'uba_axial_direction' : float(uba_axial_direction), 'uba_radiale_direction' : float(uba_radiale_direction), 'uba_tangential_direction' : float(uba_tangential_direction), 'oba_axial_direction' : float(oba_axial_direction), 'oba_radiale_direction' : float(oba_radiale_direction), 'oba_tangential_direction' : float(oba_tangential_direction), 'microphone' : float(microphone)}
    # input_dict = {'tachometer_signals' : tachometer_signals}
    input_df = pd.DataFrame([input_dict])
    # input_df = input_df.to_json()

    # working = "Working"
    # print("Working")
    # return str(input_df)
    # return_df = jsonify(predict(model=model, input_df=input_df))
    return_df = predict(model=model, input_df=input_df)
    # return_df = return_df.to_json()
    return return_df
    # return jsonify(predict(model=model, input_df=input_df))
    # return render_template('home.html')
    # return input_df
    


@app.route("/loaded_model_batch", methods=["POST"])
def loaded_model_batch():
    file = request.files['file']
    read = pd.read_csv(file)
    print(read)
    read = to_json(read)
    return jsonify(read)

# @app.route("/loaded_model_batch", methods=["GET"])
# def loaded_model_batch():
    
    # target = os.path.join(app.static_folder, '46.csv')
    # with open(target) as fp:
    #     region_map = fp.read()
    # return region_map

    # new_file = request.args.get['fileData']
    # new_file = pd.read_cvs("static_file/csv_file/47.csv")
   
    # new_file = pd.read_csv(url_for('static', filename='/csv_file/47.csv'))
   
    # predictions = predict(model=model, data = new_file)
    # return st.write(prdeictions)
    # new_file("Working")
    # return new_file

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=8080, debug=True)


# predict(take argument as a data) and return a response
#  set 
#  python flaskApp.py
# run on IP address 
# http://192.168.0.0:port/predict
# streamlit run .\Old_app.py
# python -m flask run
# wifi = MEAN
# pass:03170014082