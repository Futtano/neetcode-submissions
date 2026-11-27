class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int) -> None:
        self.available = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.available[carType] == 0:
            return False

        self.available[carType] -= 1
        return True