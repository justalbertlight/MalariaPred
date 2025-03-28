import os
import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Set page configuration
st.set_page_config(page_title="Malaria in Pregnancy Prediction",
                   layout="wide",
                   page_icon="🤰")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

malariamodel = pickle.load(open(f'{working_dir}/saved_models/malariamodelnew.sav', 'rb'))
# saved_models/malariamodelnew.sav'
#heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

#parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
#with st.sidebar:
    #


# Diabetes Prediction Page
    # page title
st.title('Malaria in Pregnancy Prediction using Machine Learning')

    # getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
        age = st.number_input('Age(How old are you?)')
with col2:
        gravida = st.number_input('Gravida (How many times have you been pregnant?)')
with col3:
        gestationalage= st.number_input('Gestational Age (How many months?)')
with col1:
        pastmalaria = 1 if st.checkbox('Past Malaria?') else 0
with col2:
        area = 1 if st.checkbox('Area?') else 0
with col3:
        fever = 1 if st.checkbox('Fever?') else 0
with col1:
        bodyaches = 1 if st.checkbox('Body Aches?') else 0
with col2:
        chills = 1 if st.checkbox('Chills?') else 0
with col3:
        difficulty = 1 if st.checkbox('Difficulty Breathing?') else 0
with col1:
        highfever = 1 if st.checkbox('High Fever?') else 0
with col2:
        profuse = 1 if st.checkbox('Profuse Sweating?') else 0
with col3:
        vomiting = 1 if st.checkbox('Vomiting?') else 0
with col1:
        severeheadache = 1 if st.checkbox('Severe Headache?') else 0
with col2:
        severechills = 1 if st.checkbox('Severe Chills?') else 0
with col3:
        howoften = st.text_input('How often')


    # code for Prediction
malariadiagnosis = ''

    # creating a button for Prediction

if st.button('Malaria Test Result'):

        inputdata = [age, gravida, gestationalage, pastmalaria, area, fever, bodyaches, chills, difficulty, highfever, profuse, vomiting, severeheadache, severechills, howoften]

        inputdata = [float(x) for x in inputdata]
        
  
        # #changng the input data to numpy array
        # inputdatanumpyarray = np.asarray(inputdata)

        # #reshape the array as we predict one instance
        # inputdatareshape = inputdatanumpyarray.reshape(1,-1)

        
        prediction = malariamodel.predict([inputdata])

        st.write(prediction)
  
        if (prediction[0]) == 0:
          malariadiagnosis = "No malaria!"
        elif (prediction[0]) == 1:
          malariadiagnosis = "You might have severe malaria"
        else:
          malariadiagnosis = "You might have uncomplicated malaria"
       
st.success(malariadiagnosis)
