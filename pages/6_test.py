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
        return [(point.latitude, point.longitude, point.elevation) for point in gpx.tracks[0].segments[0].points]

    def plot_route(self):
        m = folium.Map(location=[self.route[0][0], self.route[0][1]], zoom_start=10)
        folium.PolyLine(locations=[(lat, lon) for lat, lon, _ in self.route], color='blue').add_to(m)
        return m

    def plot_elevation_profile(self):
        elevations = [elevation for _, _, elevation in self.route]
        distances = [0]
        total_distance = 0

        for i in range(1, len(self.route)):
            lat1, lon1, _ = self.route[i - 1]
            lat2, lon2, _ = self.route[i]
            distance = self.haversine(lat1, lon1, lat2, lon2)
            total_distance += distance
            distances.append(total_distance)

        plt.plot(distances, elevations)
        plt.xlabel('Distance (m)')
        plt.ylabel('Elevation (m)')
        plt.title('Elevation Profile')
        plt.grid(True)

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        # Calculate the distance between two points on the Earth's surface using the haversine formula
        import math
        radius = 6371000  # Earth radius in meters
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat/2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return radius * c


 

    # Plot the elevation profile
    #gpx_plotter.plot_elevation_profile()
    #plt.show()


    gpx_plotter = GPXRoutePlotter('datafiles/test.gpx')

   # Plot the route on the map
    route_map = gpx_plotter.plot_route()
    route_map.save('route_map.html')
    st_data = st_folium(route_map, width=700)

    # Plot the elevation profile
    st.pyplot(gpx_plotter)
    st.pyplot(plt)