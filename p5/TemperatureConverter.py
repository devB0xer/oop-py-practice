

class TemperatureConverter:

    def __init__(self, temp):
        self.tempC = temp

    @staticmethod
    def celsiusToFarenheit(celsius: int):
        return 9/5 * celsius + 32
    
    @classmethod
    def fromKelvin(cls, kelvin: int):
        celsius = kelvin - 273.15
        return cls(celsius)