import streamlit as st
from pprint import pprint
from pcu import pcu_calculator

"""
# Dynamic PCU Estimator
"""

input1 = st.file_uploader("Input File", type="csv")
input2 = st.file_uploader("Area File", type="csv")

if input1 is not None and input2 is not None:

    with st.spinner(text="Fetching PCU"):
        dff = pcu_calculator(input1, input2)

    dff

    st.balloons()