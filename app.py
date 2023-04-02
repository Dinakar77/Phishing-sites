import streamlit as st
import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as re
import matplotlib.pyplot as plt
st.title('welcome to the phishing detection application')

St.write('This ML-baesd app is developed for educational purposes.'
          'Objective of the app is detecting phishing website only using content data.'
          'Not the URL!'
          'You can see the details of the approach, dataset, feature and results if',
          'you click on "Project Details, ')

st.table(ml.df_results)

st.write('SVM --> Support Vector Machine')
st.write('DT --> Decision Tree')
st.write('RF --> Random Forest')
st.write('KN --> K-Neighbours')

Choice = st.selection("Please select your machine learning model",
                      [
                               'Support Naive Bayas',
                               'Decision Treee',
                               'Random Forest',
                               'K-Neighbours'
                            
                      ]
                      )

if choice == 'Support Vector Machine':
    model = ml.svm_model
    st.write('SVM model is selected!')
elif choice == 'Decision Tree':
     model = ml.dt_model
     st.write('DT model is selected!')
elif choice == 'Random Forest':
     model = ml.rf_model
     st.write('RF model is selected!')
else:
    model = ml.kn.model
    st.write('KN model is selected!')

url = st.text_input('Enter the URL')

if st.button('check!'):
    try:
        response = re.get(url, verify=False, timeout=4)
        if response.status_code !=200:
            print(".HTTP connection is not sucessful for the URL: ", url)
        else:
            Soup = BeautifulSoup(response.content, "html.parser")
            vector = [fe.create_vector(soup)]
            result = model.predict(vector)


            if result[0] == 0:
                st.success("This web page seems a legitimate!")
                st.balloons()
            else:
                st.warning('Attention! This web page is a potential PHISHING!')
                st.snow()
except re.exceptions.RequesException as e;
    print("-->", e)
