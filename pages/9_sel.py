import streamlit as st
from streamlit_folium import folium_static
import folium
import requests

def get_country_color(country_name):
    # Define colors for specific countries
    country_colors = {
        "Germany": "yellow",
        "United Kingdom": "yellow",
        "Denmark": "red",
        "Australia": "red",
        "Micronesia (Federated States of)": "red",
        "French Polynesia": "red",
    }
    return country_colors.get(country_name, "blue")  # Default to blue for other countries

def main():
    # Set Streamlit app title
    st.title("Enhanced Oslo Map with Colored Countries")

    # Create a Folium map centered around Oslo
    oslo_map = folium.Map(location=[59.9139, 10.7522], zoom_start=4)

    # Add a base layer with OpenStreetMap tiles
    folium.TileLayer("openstreetmap").add_to(oslo_map)

    # Load political country boundaries GeoJSON data
    political_countries_url = (
        "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
    )
    response = requests.get(political_countries_url)
    geo_json_data = response.json()

    # Print properties of the GeoJSON features to identify the correct property name
    if geo_json_data['features']:
        feature = geo_json_data['features'][0]
        st.write("Available properties in GeoJSON:", feature['properties'].keys())

    # Mark specific countries (Germany, England, Denmark) with yellow color
    for feature in geo_json_data['features']:
        country_name = feature['properties']['name']  # Adjust the property name as needed
        if country_name in ["Germany", "United Kingdom", "Denmark"]:
            color = "yellow"
        else:
            color = "blue"  # Default color for other countries

        folium.GeoJson(
            feature,
            name=country_name,
            style_function=lambda x, color=color: {
                'fillColor': color,
                'color': 'black',
                'weight': 2,
                'fillOpacity': 0.5,
            }
        ).add_to(oslo_map)

    # Display the Folium map using folium_static
    folium_static(oslo_map)  # Use folium_static from streamlit_folium

if __name__ == "__main__":
    main()

