# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self.__celsius = value
        else:
            raise ValueError("must be greater than or equal to -273.15")

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        c = (value - 32) * 5/9
        self.__celsius = c          # ← BUG 1 fixed: was __celcius

    @property
    def kelvin(self):
        return self.__celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        if value < 0:
            raise ValueError("kelvin cant be less than 0")
        self.__celsius = value - 273.15

    @celsius.deleter
    def celsius(self):
        raise AttributeError("Temperature cannot be deleted")

    def __repr__(self):
        return (f"Temperature({self.__celsius:.2f}°C / "   # ← BUG 2 fixed
                f"{self.fahrenheit:.2f}°F / "
                f"{self.kelvin:.2f}K)")

t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0
print(t.kelvin)       # 298.15
print(repr(t))        # Temperature(25.00°C / 77.00°F / 298.15K)

t.fahrenheit = 32     # sets celsius to 0
print(t.celsius)      # 0.0

t.kelvin = 0          # sets celsius to -273.15
print(t.celsius)      # -273.15

try:
    t.celsius = -300
except ValueError as e:
    print(f"ValueError: {e}")

try:
    del t.celsius
except AttributeError as e:
    print(f"AttributeError: {e}")