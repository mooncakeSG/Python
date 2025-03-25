class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        """
        Constructor to initialize the smartphone's attributes.
        """
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours
    
    def display_info(self):
        """
        Method to display the smartphone's details.
        """
        print(f"{self.brand} {self.model} - Storage: {self.storage}GB, Battery Life: {self.battery_life} hours")
    
    def charge(self):
        """
        Method to simulate charging the smartphone.
        """
        print(f"Charging your {self.brand} {self.model}...")
    
    def make_call(self, number):
        """
        Method to simulate making a call.
        """
        print(f"Calling {number} from your {self.brand} {self.model}...")

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        """
        Constructor to initialize the gaming smartphone's attributes.
        """
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system  # True if it has a cooling system, False otherwise
    
    def play_game(self, game_name):
        """
        Method to simulate playing a game on the smartphone.
        """
        if self.cooling_system:
            print(f"Playing {game_name} on your {self.brand} {self.model} with enhanced cooling!")
        else:
            print(f"Playing {game_name} on your {self.brand} {self.model}, but it might get warm!")
    
    def display_info(self):
        """
        Overriding the display_info method to include cooling system details.
        """
        super().display_info()
        print(f"Cooling System: {'Yes' if self.cooling_system else 'No'}")

# Example usage:
if __name__ == "__main__":
    # Create a regular smartphone object
    my_phone = Smartphone("Apple", "iPhone 14", 128, 20)
    my_phone.display_info()
    my_phone.make_call("123-456-7890")
    my_phone.charge()
    print("\n---\n")
    # Create a gaming smartphone object
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 256, 15, True)
    gaming_phone.display_info()
    gaming_phone.play_game("Fortnite")