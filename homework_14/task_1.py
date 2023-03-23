class Transport:
    def __init__(self, speed, weight, passenger_count):
        """
        Initialize a Transport object with the given speed, weight, and passenger count.
        """
        self.speed = speed
        self.weight = weight
        self.passenger_count = passenger_count

    def calculate_occupancy(self, passengers):
        """
        Calculate the occupancy percentage of the transport given the number of passengers.
        Returns occupancy percentage of the transport
        """
        return (passengers / self.passenger_count) * 100


class Train(Transport):
    def __init__(self, speed, weight, passenger_count, carriage_count):
        """
        Initialize a Train object with the given speed, weight, passenger count, and carriage count.
        """
        super().__init__(speed, weight, passenger_count)
        self.carriage_count = carriage_count

    def calculate_occupancy(self, passengers, reserved_seats):
        """
        Calculate the total and reserved occupancy percentages of the train
        given the number of passengers and reserved seats.
        Returns dictionary containing the total and reserved occupancy percentages of the train.
        """
        occupancy = super().calculate_occupancy(passengers)
        reserved_occupancy = (reserved_seats / self.passenger_count) * 100
        return {'total_occupancy': occupancy, 'reserved_occupancy': reserved_occupancy}

    def get_total_weight(self):
        """
        Calculate the total weight of the train including its carriages.
        Returns total weight of the train
        """
        return self.weight + (self.carriage_count * 2000)  # assume each carriage weighs 2 tonnes


class Plane(Transport):
    def __init__(self, speed, weight, passenger_count, range_km):
        """
        Initialize a Plane object with the given speed, weight, passenger count, and range in kilometers
        """
        super().__init__(speed, weight, passenger_count)
        self.range_km = range_km

    def calculate_fuel_efficiency(self):
        """
        Calculate the fuel efficiency of the plane.
        Returns the fuel efficiency of the plane in kilometers per kilogram
        """
        return self.range_km / (self.weight * 0.001)  # assume fuel efficiency is proportional to weight


def main():
    train = Train(120, 7800, 460, 10)
    print(train.calculate_occupancy(400, 80))
    print(train.get_total_weight())

    plane = Plane(880, 15600, 315, 5000)
    print(plane.calculate_fuel_efficiency())


if __name__ == '__main__':
    main()
