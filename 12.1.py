class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print("The restaurant is now open!")

newRestaurant = Restaurant("Pizza Hut", "Italian")
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def display_flavors(self):
        print("We have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor)

newIceCreamStand = IceCreamStand("The Scoop", "Ice Cream")
newIceCreamStand.add_flavor("Chocolate")
newIceCreamStand.add_flavor("Vanilla")
newIceCreamStand.add_flavor("Strawberry")
newIceCreamStand.display_flavors()