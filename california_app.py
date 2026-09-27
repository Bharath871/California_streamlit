import numpy as np
import joblib
import streamlit as st

obj = joblib.load('california.joblib')
model = obj['model']
cols = obj['columns']

st.title('California Prediction App')
In =[]
for i in cols:
    v = st.number_input(f'Enter feature {i}:')
    In.append(v)

if st.button('click'):
    out = model.predict([In])
    st.success(f'The Median house value is: {out}')
    




