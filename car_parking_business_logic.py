from geopy.distance import geodesic


class ParkingSpot:
    def __init__(self, name, latitude, longitude, price_per_hour):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.price_per_hour = price_per_hour


class ParkingSpotManager:
    def __init__(self):
        self.parking_spots = []
        self.reservations = []

    def add_parking_spot(self, name, latitude, longitude, price_per_hour):
        spot = ParkingSpot(name, latitude, longitude, price_per_hour)
        self.parking_spots.append(spot)

    def get_all_parking_spots(self):
        return self.parking_spots

    def search_nearby_parking_spots(self, latitude, longitude, radius):
        nearby_spots = []
        user_location = (latitude, longitude)

        for spot in self.parking_spots:
            spot_location = (spot.latitude, spot.longitude)
            distance = geodesic(user_location, spot_location).meters
            if distance <= radius:
                nearby_spots.append(spot)

        return nearby_spots

    def reserve_parking_spot(self, spot_index, hours):
        if spot_index < 0 or spot_index >= len(self.parking_spots):
            return None

        spot = self.parking_spots[spot_index]
        price = spot.price_per_hour * hours

        reservation = {
            'spot': spot,
            'hours': hours,
            'price': price
        }

        self.reservations.append(reservation)
        return reservation

    def get_user_reservations(self):
        return self.reservations
