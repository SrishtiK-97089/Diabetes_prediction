# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 14:48:19 2021

@author: hp
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('model_diab.pkl', 'rb'))

def predict_default(features):


    features = np.array(features).astype(np.float64).reshape(1,-1)
    
    prediction = model.predict(features)
    probability = model.predict_proba(features)

    return prediction, probability


def main():

    html_temp = """
        <div style = "background-color: green; padding: 15px;">
            <center><h1><i>DIABETES PREDICTOR <i></h1></center>
        </div><br>
        <div style = "background-color: green; padding: 15px;">
            <center><h1><i>DEVELOPED BY Srishti Kumari<i></h1></center>
        </div><br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    pregnancies = st.text_input("No. of pregnancies") 
    
    plasma_glucose = st.text_input("Enter glucose content in plasma") 
   
    blood_pressure = st.text_input("Enter blood pressure ")           
   
    triceps_skin_thickness = st.text_input("Enter thickness of triceps skin ")
    

    insulin    = st.text_input("Insulin level ")
    
    bmi        = st.text_input("Enter you bmi ")
    
    diabetes_pedigree    = st.text_input("Diabetes pedigree")
    
    age = st.text_input("Enter your age")
    

  
    if st.button("Predict"):
        
        features = [pregnancies,plasma_glucose,blood_pressure,triceps_skin_thickness,insulin,bmi,diabetes_pedigree,age]
        prediction, probability = predict_default(features)
        # print(prediction)
        # print(probability[:,1][0])
        if prediction[0] == 1:
            # counselling_html = """
            #     <div style = "background-color: #f8d7da; font-weight:bold;padding:10px;border-radius:7px;">
            #         <p style = 'color: #721c24;'>This account will be defaulted with a probability of {round(np.max(probability)*100, 2))}%.</p>
            #     </div>
            # """
            # st.markdown(counselling_html, unsafe_allow_html=True)

            st.success("You have diabetes with a probability of {}%.".format(round(np.max(probability)*100, 2)))

        else:
            st.success("You don't have diabetes detected with a probability of having diabetes is {}%.".format(round(np.max(probability)*100, 2)))

      



if __name__ == '__main__':
    main()
