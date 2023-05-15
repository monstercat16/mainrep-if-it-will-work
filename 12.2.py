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
    def __init__(self, restaurant_name, cuisine_type, location, working_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        self.location = location
        self.working_hours = working_hours

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
        else:
            print(f"{flavor} is not available.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"{flavor} is available.")
        else:
            print(f"{flavor} is not available.")

    def display_flavors(self):
        if len(self.flavors) == 0:
            print("We don't have any flavors available at the moment.")
        else:
            print("We have the following flavors available:")
            for flavor in self.flavors:
                print("- " + flavor)

    def make_popsicle(self, flavor):
        if "popsicle" in self.cuisine_type.lower():
            print(f"Making a {flavor} popsicle!")
        else:
            print("Sorry, we don't make popsicles here.")

    def make_soft_serve(self, flavor):
        if "soft serve" in self.cuisine_type.lower():
            print(f"Making a {flavor} soft serve!")
        else:
            print("Sorry, we don't make soft serve here.")

    # Add more methods for different types of ice cream


class PopsicleStand(IceCreamStand):
    def __init__(self, restaurant_name, location, working_hours):
        super().__init__(restaurant_name, "popsicle", location, working_hours)

    def make_popsicle(self, flavor):
        print(f"Making a {flavor} popsicle!")

    # Add more methods specific to popsicle stands


class SoftServeStand(IceCreamStand):
    def __init__(self, restaurant_name, location, working_hours):
        super().__init__(restaurant_name, "soft serve", location, working_hours)

    def make_soft_serve(self, flavor):
        print(f"Making a {flavor} soft serve!")

    # Add more methods specific to soft serve stands
