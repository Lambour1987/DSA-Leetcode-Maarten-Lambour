class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType -1] > 0:
            self.spaces[carType - 1] -=1
            return True
        return False

    # Your ParkingSystem object will be instantiated and called as such:
    # obj = ParkingSystem(big, medium, small)
    # param_1 = obj.addCar(carType)

# Maak een instantie van ParkingSystem met bijvoorbeeld 3 grote, 5 middelgrote en 2 kleine parkeerplaatsen
parkeer_systeem = ParkingSystem(3, 5, 2)

# Voeg een auto van type 1 (groot) toe
resultaat = parkeer_systeem.addCar(1)
print(resultaat)  # Dit zou True moeten zijn als er nog grote parkeerplaatsen beschikbaar zijn, anders False

# Voeg een auto van type 2 (middel) toe
resultaat = parkeer_systeem.addCar(2)
print(resultaat)  # Dit zou True moeten zijn als er nog middelgrote parkeerplaatsen beschikbaar zijn, anders False

# Voeg een auto van type 3 (klein) toe
resultaat = parkeer_systeem.addCar(3)
print(resultaat)  # Dit zou True moeten zijn als er nog kleine parkeerplaatsen beschikbaar zijn, anders False

# Probeer nog een auto van type 1 (groot) toe te voegen, maar er zijn geen grote parkeerplaatsen meer
resultaat = parkeer_systeem.addCar(1)
print(resultaat)  # Dit zou False moeten zijn omdat er geen grote parkeerplaatsen meer beschikbaar zijn