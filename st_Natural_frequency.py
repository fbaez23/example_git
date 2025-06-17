#Free Vibration of a Body with Damping and Spring
# This code calculates the natural frequency of a body with damping and spring, and plots the displacement over time.
import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
##  python -m streamlit run .\st_Natural_frequency.py
# Title
st.title("Free Vibration of a Body with Damping and Spring")

# Sidebar
m = st.sidebar.number_input("What is the mass of the body:", value=1.00, format="%0.2f")
c = st.sidebar.number_input("WHat is the damping ratio:",value=1.00, format="%0.2f")
k = st.sidebar.number_input("What is the stiffness of the spring:",value=1.00, format="%0.2f")
x0 = st.sidebar.number_input("What is the initial displacement of the body:",value=0.00, format="%0.2f")
v0 = st.sidebar.number_input("What is the initial velocity of the body:",value=0.00, format="%0.2f")
time = st.sidebar.slider("Select time range:", min_value=0, max_value=10)
button = st.sidebar.button("Calculate Natural Frequency")

# Compute natural frequency and displacement
t = np.linspace(0, time, 1000)  # Time vector
wn= np.sqrt(k/m)
z = c/(2*m*wn)
wd = wn * np.sqrt(1 - z**2)
xt = np.exp(-z*wn*t) * (x0*np.cos(wd*t) + ((v0 + z*wn*x0)/wd)*np.sin(wd*t))
data = {'t': t, 'xt': xt}

# Display results
if button:
    st.write(f"Natural Frequency (wn): {wn:.2f} rad/s")
    st.write(f"Damped Frequency (wd): {wd:.2f} rad/s")
    st.write(f"Damping Ratio (z): {z:.2f}")
    # st.write(f"Displacement over time: {xt}")
# Plot the displacement over time

    fig, ax = plt.subplots()
    ax.plot(t, xt, label='Displacement X(t)')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Displacement x(t)')  
    ax.legend()
    ax.set_title('Displacement of the Body Over Time')  
    st.pyplot(fig)
    st.dataframe(data=data,width=200, height=1000)






