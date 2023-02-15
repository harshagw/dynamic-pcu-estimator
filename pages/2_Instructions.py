import streamlit as st

st.set_page_config(
    page_title="Dynamic PCU Estimator",
)

st.title("Instructions")

st.subheader("Input")

st.write(
    """
    The program takes the following inputs:
    
    1) Distance under observation: The distance on the highway where the traffic flow is being observed.
    
    2) Time interval for PCU calculation: The duration of time for which the PCU value will be calculated.
    
    3) Input file: A file containing vehicle type, entry and exit time of each vehicle for all vehicle classes.
    
    4) Area file: A file containing vehicle type, category, and area for all vehicle classes.
"""
)

st.subheader("Calculated values")

st.write(
    """
    1) Entry and Exit Flow:
    
        1.1) Cumulative Entry Flow: The total number of vehicles that have entered the distance under observation.
        
        1.2) Cumulative Exit Flow: The total number of vehicles that have exited the distance under observation.
        
        1.3) Entry Flow/Interval: The number of vehicles that have entered the distance under observation in the given time interval.
        
        1.4) Exit Flow/Interval: The number of vehicles that have exited the distance under observation in the given time interval.
    
    2) SMS (Space Mean Speed):
        
        2.1) Total Travel Time In 1 Min (Cumulative): The total travel time of all vehicles that have traveled the distance under observation.
    
        2.2) Total Travel Time In 1 Min (Interval Wise): The total travel time of all vehicles that have traveled the distance under observation in the given time interval.
    
        2.3) Average Travel Time In Every 1 Min: The average travel time of all vehicles that have traveled the distance under observation per minute.
    
        2.4) SMS: The space mean speed of all vehicles that have traveled the distance under observation.
    
        2.5) Exit Flow per hour: The number of vehicles that have exited the distance under observation per hour.
    
    3) Frequency Distribution (Traffic Composition wise): The distribution of vehicle types that have traveled the distance under observation.
    
    4) Cumulative Speed (Traffic Composition wise): The cumulative speed of each vehicle type that has traveled the distance under observation.
    
    5) Average Speed Of Vehicle Classes in the given time Intervals (Traffic Composition wise): The average speed of each vehicle type that has traveled the distance under observation in the given time interval.

"""
)

st.subheader("Output")

st.write(
    """
    1) Individual PCU Values: The PCU values for each vehicle class in each time interval.
    
    2) PCU per time interval: The total PCU value for all vehicle classes in the given time interval.
    
    3) Total PCU per hour: The total PCU value for all vehicle classes per hour.
"""
)