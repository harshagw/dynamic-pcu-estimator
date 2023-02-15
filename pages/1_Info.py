import streamlit as st

st.set_page_config(
    page_title="Dynamic PCU Estimator",
)

st.title("Estimation of Dynamic PCU")

st.write(
    """Transportation engineering is essential for designing and managing highways and roads to ensure smooth and safe traffic flow. One important metric used in transportation engineering is the Passenger Car Unit (PCU), which quantifies the impact of a vehicle on traffic flow by measuring the number of passenger cars displaced in traffic by a given vehicle. In this project, we aim to estimate the dynamic PCU on a highway based on distance, time interval, and vehicle type input.

Our project takes input data consisting of the distance under observation , time interval the vehicle spent, type of vehicle for each vehicle class and no. of lanes .Each type of vehicle is designated with a vehicle class . Using this input data, our estimation method calculates the PCU per time interval and total PCU per hour for each vehicle class.

Our estimation method takes into account the impact of different types of vehicles on traffic flow, with heavier or larger vehicles having a greater impact than smaller ones. The method uses Chandra's method, which takes into account the speeds and projected areas of the different vehicle classes to calculate the PCU per time interval and total PCU per hour.

Accurate PCU estimation is critical for transportation engineering, as it provides important insights into traffic flow patterns and helps in designing and managing highways and roads. By understanding the impact of different types of vehicles on traffic flow, engineers can make informed decisions about road widening, lane addition, traffic signal timings, and other interventions that can help improve traffic flow and reduce congestion. 

"""
)
