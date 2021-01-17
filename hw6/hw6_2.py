
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_mass(self, mass_meter, thickness):
        self.mass_meter = mass_meter
        self.thickness = thickness
        total_mass = self._length * self._width * mass_meter * thickness / 1000
        print(f"Масса асфальта, необходимая для покрытия всего дорожного полотна: {total_mass} тонн")

main_road = Road(20, 5000)
main_road.asphalt_mass(25, 5)