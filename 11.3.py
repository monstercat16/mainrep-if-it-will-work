class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type of the restaurant is {self.cuisine_type}.")
        print(f"The rating of the restaurant is {self.rating}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

    def set_rating(self, new_rating):
        self.rating = new_rating
        print(f"The rating of the restaurant has been updated to {self.rating}.")

# Создание экземпляра класса Restaurant
newRestaurant = Restaurant("Italiano", "Italian")

# Вывод атрибутов по отдельности
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

# Вызов методов
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

# Установка и вывод нового рейтинга
newRestaurant.set_rating(4.5)
newRestaurant.describe_restaurant()