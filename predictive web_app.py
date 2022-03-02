import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)



import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('C:/Users/user/Muqesh.py/Office/HR Analysis/trained_model.sav', 'rb'))

# Creating supporting function
def attrition_prediction(input_data):
   
    input_data = np.asarray(input_data).reshape(1,-1)
    prediction = loaded_model.predict(input_data)
    print(prediction)

    if prediction[0]==0:
        return 'Not Attrited'
    elif prediction[0]==1:
        return 'Attrited'
    
    
def main():
    
    # giving title
    st.title('Employee Attrition Prediction')
    
    # Getting input data
    
    YearsAtCompany = st.number_input('Years At Company', min_value=0, max_value=60)
    StockOptionLevel = st.selectbox('Stock Level', [0,1,2,3])
    YearsWithCurrManager = st.number_input('Years with Current Manager', min_value=0, max_value=60)
    Age = st.slider('Age of the employee', min_value=18, max_value=60)
    MonthlyIncome = st.number_input('Monthly Salay', min_value=0, max_value=20000)
    YearsInCurrentRole = st.number_input('Years In Current JobRoll', min_value=0, max_value=60)
    JobLevel = st.radio('Job Level "1:Lowest, 5:Highest"', [1,2,3,4,5])
    TotalWorkingYears = st.number_input('Total Working Years', min_value=0, max_value=60)
    MaritalStatus = st.selectbox('Marital Status "1:Married, 2:Single, 3:Divorced', [1, 2, 3])
    OverTime = st.radio('Over Time "1:Yes, 0:No"', [1,0])
    
    
    # Prediction
    results = ''
    
    # Creating Button for result
    if st.button('Result'):
        results = attrition_prediction([Age, YearsAtCompany, StockOptionLevel, YearsWithCurrManager, MonthlyIncome,
                                       YearsInCurrentRole,  MaritalStatus, JobLevel, TotalWorkingYears, OverTime])
    st.success(results)
    

if __name__ == '__main__':
    main()