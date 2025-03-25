import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Malaria in Pregnancy Prediction",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

malariamodel = pickle.load(open(f'{working_dir}/saved_models/malariamodel.sav', 'rb'))

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
        age = st.text_input('Age')
with col2:
        gravida = st.text_input('Gravida')
with col3:
        gestationalage= st.text_input('GestAge')
with col1:
        pastmalaria = st.text_input('PastMalaria')
with col2:
        area = st.text_input('Area')
with col3:
        fever = st.text_input('Fever')
with col1:
        bodyaches= st.text_input('bodyaches')
with col2:
        chills = st.text_input('chills')
with col3:
        difficulty = st.text_input('difficulty')
with col1:
        highfever = st.text_input('high fever')
with col2:
        profuse = st.text_input('Profuse Sweating')
with col3:
        vomiting = st.text_input('Vomiting')
with col1:
        severeheadache = st.text_input('Severe Headache')
with col2:
        severechills = st.text_input('Severe chills')
with col3:
        howoften = st.text_input('How often')


    # code for Prediction
malariadiagnosis = ''

    # creating a button for Prediction

if st.button('Malaria Test Result'):

        user_input = [age, gravida, gestationalage, pastmalaria, area, fever, bodyaches, chills, difficulty, highfever, profuse, vomiting, severeheadache, severechills, howoften]

        user_input = [float(x) for x in user_input]

        prediction = malariamodel.predict([user_input])
        #print(malariadiagnosis)

        if prediction[0] == 0:
          malariadiagnosis = "Congrats, you are free!"
        elif prediction[0] == 1:
          malariadiagnosis = "You might have malaria"
        elif prediction[0] == 2:
          malariadiagnosis = "You really have malaria"
        else:
          malariadiagnosis = "There is an error somewhere"
st.success(malariadiagnosis)
