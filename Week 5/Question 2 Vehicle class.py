import sys
import io

# Set the default encoding to UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)

class Vehicle:
    def move(self):
        """
        Base method to define movement.
        """
        print("This vehicle is moving.")

class Car(Vehicle):
    def move(self):
        """
        Overrides the move method for cars.
        """
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        """
        Overrides the move method for planes.
        """
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        """
        Overrides the move method for boats.
        """
        print("Sailing ⛵")

def transport(vehicle):
    """
    Takes any vehicle object and calls its move method.
    """
    vehicle.move()

# Example usage:
if __name__ == "__main__":
    car = Car()
    plane = Plane()
    boat = Boat()
    
    # Using polymorphism
    print("Car:")
    transport(car)
    print("\nPlane:")
    transport(plane)
    print("\nBoat:")
    transport(boat)