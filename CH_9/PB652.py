class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        # Default fare: capacity * 100
        return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
        # Get the base fare from the Parent class
        base_fare = super().fare()
        # Add 10% maintenance charge
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare
# 1. Bus Instance
school_bus = Bus("School Bus", 12, 50)
print(f"Vehicle: {school_bus.name}")
print(f"The bus seating capacity is {school_bus.capacity}. "
      f"So, the final fare amount should be {school_bus.fare()}")
# 2. Car Instance 
car = Vehicle("Car", 20, 5)
print(f"\nVehicle: {car.name}")
print(f"The car seating capacity is {car.capacity}. "
      f"So, the final fare amount should be {car.fare()}")