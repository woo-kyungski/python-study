import crawling
import folium
from geopy.geocoders import Nominatim

def drawing_map(url):
    sites = crawling.crawling_sites(url)
    map = folium.Map(location = [27.333, 3.252], zoom_start = 2) # folium 생성 : 중심 위도 27.333 / 중심 경도3.252
    geolocator = Nominatim(user_agent="travel")
    
    for site in sites:
        if site == 'Canadian High Arctic': # 74.75, 265.00
            location = [74.75, 265.00]
        else:
            popup = f'{site}'
            location_info = geolocator.geocode(site)
            location = [location_info.latitude, location_info.longitude]
            folium.Marker(
                location = location,
                popup = popup
            ).add_to(map)

    return map