import streamlit as st
import pandas as pd
from pcu import pcu_calculator
import math

st.set_page_config(
    page_title="Dynamic PCU Estimator",
)

st.title("Dynamic PCU Estimator")

distance = st.number_input(step=1, min_value=1, value=62, label="Distance")
interval = st.number_input(step=60, min_value=60, value=300, label="Time Interval")
input1 = st.file_uploader("Input File", type="csv")
input2 = st.file_uploader("Area File", type="csv")

if input1 is not None and input2 is not None and distance is not None and interval is not None:
    st.markdown("""---""")

    st.header("Result are as follow - ")

    with st.spinner(text="Loading..."):
        df = pd.read_csv(input1)
        areas = pd.read_csv(input2)
        input1.seek(0)
        input2.seek(0)

        if "Category" not in areas.columns or "Vehicle Type" not in areas.columns or "Area" not in areas.columns:
            st.error(
                "Please check the Area File. It should contain 'Category', 'Vehicle Type' and 'Area' columns. Please reload")
            st.stop()

        if "Vehicle Type" not in df.columns or "Entry" not in df.columns or "Exit" not in df.columns:
            st.error(
                "Please check the Input File. It should contain 'Vehicle Type', 'Entry' and 'Exit' columns. Please reload")
            st.stop()

        output = pcu_calculator(input1, input2, distance, interval)

        output_csv_file = output.to_csv().encode('utf-8')

    for j in range(0, areas.shape[0]):
        pcu_sum = 0

        time_interval_last_value = math.ceil(output.iloc[-1]['Exit'])
        total = math.ceil(time_interval_last_value / interval)

        for i in range(0, total):
            pcu_sum += output.at[i, areas.at[j, 'Category'] + ' Individual PCU Values in each time Interval']

        pcu_sum /= total

        st.text(f"{areas.at[j, 'Category']} - Average PCU is {pcu_sum}")

    st.markdown("""---""")
    st.header("Full Output - ")

    st.dataframe(output)

    st.download_button(label="Download the Output", data=output_csv_file, file_name='final_output.csv', mime='text/csv')
