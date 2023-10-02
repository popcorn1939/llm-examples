import streamlit as st
from io import BytesIO
from PIL import Image
import time
import folium

st.write("hej med dig11111")


# Create a function to capture the Folium map as an image using time delay
def capture_folium_map(map):
    st.write("hej 6er")
    # Create a temporary HTML file to save the Folium map
    map.save("datafiles/oslo_map1.html")

    # Set up a Streamlit iframe to display the HTML file
    st.components.v1.iframe("datafilesoslo_map1.html", height=600)

    # Wait for the iframe to load (adjust the delay if needed)
    #time.sleep(5)

    # Take a screenshot of the Streamlit app using the browser's print screen
    #st.image("datafiles/screenshot.png")
    #st.write("done")


st.write("hej 4er")
# Create a map centered at Oslo, Norway

oslo_map = folium.Map(location=[59.9139, 10.7522], zoom_start=14)

# You can add markers, circles, or any other elements to the map if needed

# Capture the Folium map as an image
capture_folium_map(oslo_map)