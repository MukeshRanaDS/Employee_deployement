import numpy as np
import pickle

# Loading Model
loaded_model = pickle.load(open('C:/Users/user/Muqesh.py/Office/HR Analysis/trained_model.sav', 'rb'))

input_data = ( 32,     1,  1005,     1,     2,     2,     1,     4,     1,
          79,     3,     1,     2,     4,     2,  3068, 11864,     0,
           0,    13,     3,     3,     0,     8,     2,     2,     7,
           7,     3,     6)
input_data = np.asarray(input_data).reshape(1,-1)
prediction = loaded_model.predict(input_data)

if prediction[0]==0:
    print('Not Attrited')
elif prediction[0]==1:
    print('Attrited')