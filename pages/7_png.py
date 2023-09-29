import folium
import streamlit as st
from io import BytesIO
from PIL import Image
import time

# Create a Streamlit app title
st.title("Folium Map in Streamlit with PIL")

# Create a function to capture the Folium map as an image using time delay
def capture_folium_map(map):
    st.write("hej")
    # Create a temporary HTML file to save the Folium map
    #map.save("oslo_map.html")

    # Set up a Streamlit iframe to display the HTML file
    #st.components.v1.iframe("oslo_map.html", height=600)

    # Wait for the iframe to load (adjust the delay if needed)
    #time.sleep(5)

    # Take a screenshot of the Streamlit app using the browser's print screen
    #st.image("datafiles/screenshot.png")
    #st.write("done")
# Create a map centered at Oslo, Norway
oslo_map = folium.Map(location=[59.9139, 10.7522], zoom_start=14)

# You can add markers, circles, or any other elements to the map if needed

# Capture the Folium map as an image
capture_folium_map(oslo_map)
