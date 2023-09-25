import streamlit as st
import gpxpy
import gpxpy.gpx
import matplotlib.pyplot as plt
import folium

st.title("🦜🔗 Langchain Quickstart App 1234")

# Load the GPX file
gpx_file = open('datafiles/test.gpx', 'r')
gpx = gpxpy.parse(gpx_file)

# Extract route coordinates
route = gpx.tracks[0].segments[0].points
latitudes = [point.latitude for point in route]
longitudes = [point.longitude for point in route]

# Create a scatter plot of the route
plt.scatter(longitudes, latitudes, color='blue', s=5)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Route from GPX File')
plt.grid()

# Show the plot
#plt.show()
st.pyplot(plt)



#import streamlit as st
#import matplotlib.pyplot as plt
#import numpy as np

#arr = np.random.normal(1, 1, size=100)
#fig, ax = plt.subplots()
#ax.hist(arr, bins=20)

#st.pyplot(fig)

#st.title("🦜🔗 Langchain Quickstart A123")