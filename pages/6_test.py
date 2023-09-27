import streamlit as st
import gpxpy
import gpxpy.gpx
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium, folium_static
from io import BytesIO
import base64

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
        self.elevation_data = self.extract_elevation_data()

    def load_gpx_route(self):
        gpx_file = open(self.gpx_file_path, 'r')
        gpx = gpxpy.parse(gpx_file)
        return [(point.latitude, point.longitude) for point in gpx.tracks[0].segments[0].points]

    def extract_elevation_data(self):
        gpx_file = open(self.gpx_file_path, 'r')
        gpx = gpxpy.parse(gpx_file)
        elevation_data = [point.elevation for point in gpx.tracks[0].segments[0].points]
        return elevation_data

    def plot_route(self):
        m = folium.Map(location=[self.route[0][0], self.route[0][1]], zoom_start=10)
        folium.PolyLine(locations=self.route, color='blue').add_to(m)
        return m
    
    def save_route_image(self, file_path):
        route_map = self.plot_route()
        route_map.save(file_path)

    def plot_elevation_profile(self):
        plt.figure(figsize=(8, 4))
        plt.plot(range(len(self.elevation_data)), self.elevation_data, color='green')
        plt.xlabel('Distance (Points)')
        plt.ylabel('Elevation (meters)')
        plt.title('Elevation Profile')


        # Save the elevation plot as an image
        img_stream = BytesIO()
        plt.savefig(img_stream, format='png')
        img_stream.seek(0)

        # Display the elevation plot as an image in Streamlit
        st.image(img_stream, caption='Elevation Profile', use_column_width=True)


# Streamlit app
st.title('GPX Route Plotter with Elevation Profile')

gpx_file_path = 'datafiles/test.gpx'  # Modify the path accordingly
gpx_plotter = GPXRoutePlotter(gpx_file_path)

st.subheader('Route Map')
m = gpx_plotter.plot_route()
st_data = st_folium(m, width=700)
#st.write(route_map._repr_html_(), unsafe_allow_html=True)

st.subheader('Elevation Profile')
gpx_plotter.plot_elevation_profile()

gpx_plotter.save_route_image('route_map.jpg')