import streamlit as st

st.set_page_config(
    page_title="Dynamic PCU Estimator",
)

st.title("Estimation of Dynamic PCU")

st.write(
    """Passenger Car Unit (PCU) is a metric used in Transportation Engineering, to assess traffic-flow rate on a highway. It is a measure of the impact that a mode of transport has on traffic variables.

It can be defined as the number of passenger cars displaced in the traffic flow by a truck or a bus, under prevailing roadway and traffic conditions or the number of passenger cars which will result in the same operational condition as a single heavy vehicle of a particular type under specified roadway, traffic and control conditions.

The project focuses on the estimation of dynamic PCU using data consisting of entry and exit time of individual vehicles and projected area of these vehicle classes. PCU per 5 minute interval and Total PCU per hour is estimated using the data for 7 different vehicle classes i.e Small Car, Big Car, Two Wheeler, LCV, Bus, Single Axle and Multi Axle.
The program uses Chandra's method for PCU estimation which uses speeds and projected areas of different vehicle classes.
"""
)
