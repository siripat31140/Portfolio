from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np


model = load_model('deployment_28042020')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return 

def user_input_features():
    island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
    sex = st.sidebar.selectbox('Sex',('male','female'))
    bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
    bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
    flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
    body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
        
    data = {'island': island,
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex}
    features = pd.DataFrame(data, index=[0])
    return features
        

def run():
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('This app is created to predict Penguins Species')
    
    st.title("Penguins Species Prediction App")
    st.write('งานนี้เป็นงานที่นำ model มาพัฒนาให้เกิด Web Application ในการทำนาย Penguins Species ซึ่งสามารถอัปโหลดไฟล์ CSV หรือทำนายที่ละเเถวข้อมูล ')
    st.write('https://github.com/siripat31140/Portfolio')

    if add_selectbox == 'Online':

        output=""
        
        input_df = user_input_features()

        if st.button("Predict"):
            output = predict_model(model,input_df)
            output = '   ' + str(predict_model(model,input_df)['Label'][0])

        st.write(input_df)
        st.success('The output is {}'.format(output))

    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)



if __name__ == '__main__':
    run()