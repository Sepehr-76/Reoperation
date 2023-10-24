from pycaret.classification import * 
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('lr')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, raw_score=True, data=input_df)
    predictions = predictions_df['prediction_score_1'][0]
    return predictions

def run():

    from PIL import Image
    image_hospital = Image.open('tehran.jpg')



    st.sidebar.info('This app is created by Sepehr Nayebirad to predict reoperation due to bleeding after CABG surgery')

    
    st.sidebar.image(image_hospital)

    st.title("Reoperation Prediction App")

    Age = st.number_input('Age', min_value=1, max_value=100, value=25)
    Hgb	 = st.number_input('Hgb', min_value=1.00, max_value=50.00, value=13.00,step=1.,format="%.2f")
    Cr	 = st.number_input('Cr', min_value=0.01, max_value=50.00, value=1.00,step=1.,format="%.2f")
    Gender = st.selectbox('Gender', ['male', 'female'])
    if Gender == 'male':
        Gender=1
    else:
         Gender=0
    NumOfProducts = st.selectbox('History of CAD disease', [0,1,2,3,4,5,6,7,8,9,10])
    if st.checkbox('Diabetes'):
        Diabetes = 1
    else:
        Diabetes = 0
    if st.checkbox('Positive family history'):
        Positive_family_history = 1
    else:
        Positive_family_history = 0
    if st.checkbox('Dyslipidemia'):
        Dyslipidemia = 1
    else:
        Dyslipidemia = 0
    if st.checkbox('Current cigarette smoking'):
        smoker = 1
    else:
        smoker = 0
    if st.checkbox('Current opium consumption'):
        opium = 1
    else:
        opium = 0
    if st.checkbox('Hx of Angioplasty POBA'):
        poba = 1
    else:
        poba = 0
    if st.checkbox('Hx of renal failure'):
        renal_failure = 1
    else:
        renal_failure = 0
    if st.checkbox('Previous antiplatelet use'):
        antiplatelet = 1
    else:
        antiplatelet = 0
    if st.checkbox('LM involvement'):
        lm = 1
    else:
        lm = 0
    if st.checkbox('Urgent/emergent surgery'):
        emergent = 1
    else:
        emergent = 0
    if st.checkbox('Off-pump surgery'):
        offpump = 1
    else:
        offpump = 0
    if st.checkbox('Cabg+valve surgery'):
        valve = 1
    else:
        valve = 0
    mi = st.selectbox('time of MI', ['MI <24h', '1d < MI < 7d', 'other'])
    if mi == 'MI <24h':
        mi24, mi1_7 = 1, 0
    elif mi == '1d < MI < 7d':
        mi24, mi1_7 = 0, 1
    elif mi == 'other':
        mi24, mi1_7 = 0, 0

    output=""

    input_dict = {'Gender' : Gender, 'Diabetes':Diabetes, 'Positive family history':Positive_family_history,
                  'Dyslipidemia' : Dyslipidemia,'Current cigarette smoking' : smoker,'Current opium consumption' : opium,
                  'Hx of Angioplasty POBA' : poba, 'Hx of renal failure' : renal_failure,
                  'Dyslipidemia' : Dyslipidemia, 'MI <24h': mi24, '1d < MI < 7d': mi1_7, 
                  'Previous antiplatelet use' : antiplatelet, 'LM involvement':lm,
                  'Age': Age, 'Hgb': Hgb, 'Cr':Cr, 'Urgent/emergent surgery':emergent, 
                  'Off-pump surgery': offpump, 'Cabg+valve surgery': valve,
}
    input_df = pd.DataFrame([input_dict])

    if st.button("Predict"):
        output = predict(model=model, input_df=input_df)
        output = 100*output

    st.success('Reoperation risk due to bleeding is {}'.format(output)+'%')

run()
