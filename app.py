# creating our webapp
#['Processor_Speed', 'RAM_Size', 'Storage_Capacity']
import streamlit as st
import numpy as np
import joblib
model=joblib.load('rf_model.pkl')

st.title("Laptop Price Prediction")

st.divider()

st.write("You can use this prediction web app after uploading you requirement parameters like processor size, ram size, storage capacity  and get the estimated laptop price")

st.divider()

processor_speed=st.number_input("Enter Processor Speed",value=2.50,step=0.50)
ram_size=st.number_input("Enter RAM Size",value=16,step=8)
storage_capacity=st.number_input("Enter Storage Capacity",value=512,step=256)

X=[processor_speed,ram_size,storage_capacity]

st.divider()

prediction = st.button("Price Estimation")

st.divider()

if prediction:
    st.balloons()
    x1=np.array(X)
    prediction=model.predict([x1])[0]
    st.write(f"The Estimated Price is : {prediction:,.2f}")
else:
    st.write("Click again to Predict and check your parameters")

