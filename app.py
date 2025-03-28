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


age = st.number_input('Age', min_value=15, max_value=50, step=1)
gravida = st.number_input('Gravida', min_value=1, max_value=20, step=1)
gestationalage = st.number_input('Gestational Age (months)', min_value=1, max_value=9, step=1)
pastmalaria = st.radio("Past Malaria?", 
                           ["No", "Yes", "Not Sure"], 
                           index=0)  # Default: "No"
area = 1 if st.checkbox('Area?') else 0
fever = 1 if st.checkbox('Fever?') else 0
bodyaches = 1 if st.checkbox('Body Aches?') else 0
chills = 1 if st.checkbox('Chills?') else 0
difficulty = 1 if st.checkbox('Difficulty Breathing?') else 0
highfever = 1 if st.checkbox('High Fever?') else 0
profuse = 1 if st.checkbox('Profuse Sweating?') else 0
vomiting = 1 if st.checkbox('Vomiting?') else 0
severeheadache = 1 if st.checkbox('Severe Headache?') else 0
severechills = 1 if st.checkbox('Severe Chills?') else 0
howoften = st.radio("How often do you get tested?", 
                        ["Never", "Occasionally", "Frequently"], 
                        index=0)  # Default: "Never"
# Convert "Past Malaria" to numerical values
pastmalaria_map = {"No": 0, "Yes": 1, "Not Sure": 2}
pastmalaria_value = pastmalaria_map[pastmalaria]

# Convert "How often" to numerical values
howoften_map = {"Never": 0, "Occasionally": 1, "Frequently": 2}
howoften_value = howoften_map[howoften]


# code for Prediction
malariadiagnosis = ''

# creating a button for Prediction

if st.button('Malaria Test Result'):

        inputdata = [age, gravida, gestationalage, pastmalaria_value, area, fever, bodyaches, chills, difficulty, highfever, profuse, vomiting, severeheadache, severechills, howoften_value]

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
