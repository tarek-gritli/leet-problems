# Runtime: 97ms, Beats 88.69% of users with Python3
# Memory: 17.04MB, Beats 40.35% of users with Python3

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small

    def addCar(self, carType: int) -> bool:
        match carType:
            case 1:
                if self.big:
                    self.big-=1
                    return True
                return False
            case 2:
                if self.medium:
                    self.medium-=1
                    return True
                return False
            case 3:
                if self.small:
                    self.small-=1
                    return True
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)