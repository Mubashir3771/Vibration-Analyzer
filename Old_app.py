from pycaret.classification import *
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
from flask import request
import os

def run():
    
    image = Image.open("D:\University_Projects\Vibration_Analyzer\images\VA.png")
    image_mafaulda = Image.open("D:\University_Projects\Vibration_Analyzer\images\Mafaulda.png")

    # st.image(image,use_column_width=False)

    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.image(image,use_column_width=True)
    

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('This app is created to predict machinery faults')
    
    st.sidebar.image(image_mafaulda)
    st.sidebar.success('https://www02.smt.ufrj.br/~offshore/mfs/page_01.html#SEC1')

    # st.title("Machinery Faults Prediction App")

    st.markdown("<h1 style='text-align: center; color: white;'>Machinery Faults Prediction App</h1>", unsafe_allow_html=True)



    if add_selectbox == 'Online':
        tachometer_signals = st.number_input('Tachometer', min_value=-1.0, max_value=1.0, value=0.0, format="%.4f")
        uba_axial_direction = st.number_input('Underhang Bearing Accelerometer Axial Direction', min_value=-1.0, max_value=1.0, value=0.0, format="%.4f")
        uba_radiale_direction = st.number_input('Underhang Bearing Accelerometer Radiale Direction', min_value=-1.0, max_value=1.0, value=0.0, format="%.4f")
        uba_tangential_direction = st.number_input('Underhang Bearing Accelerometer Tangential Direction', min_value=-1.0, max_value=1.0, value=0.0, format="%.4f")
        oba_axial_direction = st.number_input('Overhang Bearing Accelerometer Axial Direction', min_value=-1.0, max_value=1.0, value=0.0, format="%.4f")
        oba_radiale_direction = st.number_input('Overhang Bearing Accelerometer Radiale Direction', min_value=-1.0, max_value=1.0, value=0.0, format="%.4f")
        oba_tangential_direction = st.number_input('Overhang Bearing Accelerometer Tangential Direction', min_value=-1.0, max_value=1.0, value=0.0, format="%.4f")
        microphone = st.number_input('Microphone', min_value=-1.0, max_value=1.0, value=0.0, format="%.4f")
        
        output=""

        #copied
        # input_dict = {'tachometer_signals' : tachometer_signals, 'uba_axial_direction' : uba_axial_direction, 'uba_radiale_direction' : uba_radiale_direction, 'uba_tangential_direction' : uba_tangential_direction, 'oba_axial_direction' : oba_axial_direction, 'oba_radiale_direction' : oba_radiale_direction, 'oba_tangential_direction' : oba_tangential_direction, 'microphone' : microphone}
        # input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            # output = request.get("http://127.0.0.1:5000/loaded_model"+ tachometer_signals + uba_axial_direction + uba_radiale_direction + uba_tangential_direction + oba_axial_direction + oba_radiale_direction + oba_tangential_direction + microphone)
            output = requests.get("http://127.0.0.1:5000/loaded_model1?tachometer_signals="+str(tachometer_signals)+"&uba_axial_direction="+str(uba_axial_direction)+"&uba_radiale_direction="+str(uba_radiale_direction)+"&uba_tangential_direction="+str(uba_tangential_direction)+"&oba_axial_direction="+str(oba_axial_direction)+"&oba_radiale_direction="+str(oba_radiale_direction)+"&oba_tangential_direction="+str(oba_tangential_direction)+"&microphone="+str(microphone))
            output = '$' + str(output.text)
            print(output)

        st.success('The output is {}'.format(output))

    if add_selectbox == 'Batch':

        # file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        file = st.file_uploader("Upload a file:")
        if file is not None:
            st.write("You uploaded:", file.name)

            url = "http://127.0.0.1:5000/loaded_model_batch"
            file_name = file.name
            # file_data = open(file_name, 'rb')
            r = requests.post(url, files={'file': file})

            output = r
            output_df = pd.DataFrame([output])
            st.write(r.text)



        # if file_upload is not None:
            
            # data = pd.read_csv(file_upload)
            # data = file_upload
            # Call api andreturn result to redictions
            # predictions = API
            # files = {'file' = data, 'rb'}

            # new_data = requests.get("http://127.0.0.1:5000/loaded_model_batch")

            # print(new_data.text)
            # predictions = predict_model(estimator=model,data=data)
            # st.write(predictions)

            # output = new_data
            # output_df = pd.DataFrame([output])
            # st.write(output_df.head(1))

#copied
# def predict(model, input_df):
#     predictions_df = predict_model(estimator = model, data = input_df)
#     predictions = predictions_df['Label'][0]
#     return predictions

if __name__ == '__main__':
    run()