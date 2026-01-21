class Distance:
    units = {'cm': 0.01, 'm': 1, 'km': 1000}

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_meters(self):
        return self.value * Distance.units[self.unit]

    def __str__(self):
        return f'{self.value} {self.unit}'

    def __add__(self, other):
        total_meters = self.to_meters() + other.to_meters()
        new_value = total_meters / Distance.units[self.unit]
        return Distance(new_value, self.unit)

    def __sub__(self, other):
        total_meters = self.to_meters() - other.to_meters()
        new_value = total_meters / Distance.units[self.unit]
        return Distance(new_value, self.unit)


d1 = Distance(8, 'm')
d2 = Distance(4, 'km')

print(d1)
print(d2)
print(d1 + d2)
print(d2 - d1)