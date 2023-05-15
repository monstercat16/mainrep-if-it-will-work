class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} - {self.cuisine_type}")

# Создание экземпляров класса
restaurant1 = Restaurant("PizzaMia", "Italian")
restaurant2 = Restaurant("SushiTime", "Japanese")
restaurant3 = Restaurant("TacoLoko", "Mexican")

# Вызов метода describe_restaurant() для каждого экземпляра
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()