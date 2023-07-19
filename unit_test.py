import unittest

from .car_parking_business_logic import ParkingSpotManager


class ParkingSpotManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.manager = ParkingSpotManager()
        self.manager.add_parking_spot('Spot 1', 18.5204, 73.8567, 10)
        self.manager.add_parking_spot('Spot 2', 18.5200, 73.8570, 8)
        self.manager.add_parking_spot('Spot 3', 18.5199, 73.8565, 12)

    def test_get_all_parking_spots(self):
        spots = self.manager.get_all_parking_spots()
        self.assertEqual(len(spots), 3)

    def test_search_nearby_parking_spots(self):
        nearby_spots = self.manager.search_nearby_parking_spots(18.5203, 73.8568, 500)
        self.assertEqual(len(nearby_spots), 2)

    def test_reserve_parking_spot(self):
        reservation = self.manager.reserve_parking_spot(1, 3)
        self.assertIsNotNone(reservation)
        self.assertEqual(len(self.manager.get_user_reservations()), 1)

    def test_get_user_reservations(self):
        self.manager.reserve_parking_spot(0, 2)
        self.manager.reserve_parking_spot(2, 1)
        reservations = self.manager.get_user_reservations()
        self.assertEqual(len(reservations), 2)


if __name__ == '__main__':
    unittest.main()
