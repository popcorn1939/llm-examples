import streamlit as st
import gpxpy
import gpxpy.gpx
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium, folium_static

st.title("🦜🔗 Langchain Quickstart App 123456789")
st.write("skrevet fra vsc september")
st.write("skrevet fra vsc september 25 abcd")
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






class GPXRoutePlotter:
    def __init__(self, gpx_file_path):
        self.gpx_file_path = gpx_file_path
        self.route = self.load_gpx_route()

    def load_gpx_route(self):
        gpx_file = open(self.gpx_file_path, 'r')
        gpx = gpxpy.parse(gpx_file)
        return [(point.latitude, point.longitude) for point in gpx.tracks[0].segments[0].points]

    def plot_route(self):
        m = folium.Map(location=[self.route[0][0], self.route[0][1]], zoom_start=10)
        folium.PolyLine(locations=self.route, color='blue').add_to(m)
        return m


gpx_plotter = GPXRoutePlotter('datafiles/test.gpx')
route_map = gpx_plotter.plot_route()
st_data = st_folium(route_map, width=700)

