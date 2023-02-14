import streamlit as st

st.set_page_config(
    page_title="Dynamic PCU Estimator",
)

st.title("Instructions")

st.subheader("Input")

st.write(
    """
    1. Distance traveled by each vehicle(equal for all) -
    2. Vehicle Type - 
    3. Entry time of each vehicle - 
    4. Exit time of each vehicle - 

    Using this data other values are calculated including:
    
    1.Entry and Exit Flow
        Cumulative Entry Flow - 
        Cumulative Exit Flow - 
        Entry Flow/Interval - 
        Exit Flow/Interval - 
        
    2.SMS(Space Mean Speed)
        Total Travel Time In 1 Min (Cumulative) - 
        Total Travel Time In 1 Min (Interval Wise) - 
        Average Travel Time In Every 1 Min - 
        SMS -  
        Exit FLow per hour - 
        
    3.Frequency Distribution (Traffic Composition wise)
    
    4.Cumulative Speed (Traffic Composition wise)
    
    5.Average Speed Of Vehicle Classes in 5 Minute Intervals (Traffic Composition wise)
"""
)

st.subheader("Area File")

st.write(
    """
    1. Distance traveled by each vehicle(equal for all) -
    2. Vehicle Type - 
    3. Entry time of each vehicle - 
    4. Exit time of each vehicle - 
"""
)