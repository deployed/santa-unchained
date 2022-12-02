import requests


class ModelMapMixin:
    def find_lat_lng(self):
        """
        Find location in OpenStreetMap and return coordinates.
        If API fail or not return any results, we return default coordinates 0, 0
        """
        default_lat_lng = (0, 0)
        try:
            url = (
                f"https://nominatim.openstreetmap.org/search.php?q={self}&format=jsonv2"
            )
            data = requests.get(url).json()
        except requests.exceptions.RequestException:
            return default_lat_lng
        if not data:
            return default_lat_lng
        lat = data[0].get("lat", 0)
        lng = data[0].get("lon", 0)
        return lat, lng
